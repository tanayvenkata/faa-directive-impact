"""Call a model once for a structured answer, and record or replay the call.

A request has three parts, in cache order:

1. ``instructions`` — fixed for a whole run;
2. ``document`` — the source text, shared by every engine screened against it.
   A cache breakpoint sits here, so after the first call each later engine
   reads the instructions and document from the prompt cache;
3. ``question`` — the per-engine part, after the breakpoint.

The answer is constrained to ``output_schema`` with structured outputs.
Refusals are recorded as results, not retried on another model: a fallback
would hide which model answered.
"""

import hashlib
import json
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Protocol

from faa_directive_impact.llm.pricing import cost_usd


@dataclass(frozen=True)
class ModelRequest:
    model: str
    instructions: str
    document: str
    question: str
    output_schema: dict[str, Any]
    effort: str = "medium"
    max_tokens: int = 16000

    def params(self) -> dict[str, Any]:
        """The Messages API parameters for this request."""
        return {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "system": [
                {"type": "text", "text": self.instructions},
                {
                    "type": "text",
                    "text": self.document,
                    "cache_control": {"type": "ephemeral"},
                },
            ],
            "messages": [{"role": "user", "content": self.question}],
            "output_config": {
                "effort": self.effort,
                "format": {"type": "json_schema", "schema": self.output_schema},
            },
        }

    def key(self) -> str:
        """A stable hash of everything sent to the model."""
        canonical = json.dumps(self.params(), sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


@dataclass
class ModelResponse:
    request_key: str
    model: str
    stop_reason: str | None
    text: str
    answer: dict[str, Any] | None
    usage: dict[str, Any]
    cost_usd: float
    latency_seconds: float
    request_id: str | None = None
    batch: bool = False
    error: str | None = None
    extra: dict[str, Any] = field(default_factory=dict)


class Model(Protocol):
    def call(self, request: ModelRequest) -> ModelResponse: ...


class MissingRecording(LookupError):
    """A replayed run asked for a call that was never recorded."""


class LiveModel:
    """Calls the Anthropic Messages API. Credentials come from the environment."""

    def __init__(self, client: Any = None) -> None:
        if client is None:
            import anthropic

            client = anthropic.Anthropic()
        self._client = client

    def call(self, request: ModelRequest) -> ModelResponse:
        started = time.monotonic()
        message = self._client.messages.create(**request.params())
        latency = time.monotonic() - started
        return response_from_message(
            request, message.to_dict(), latency, message._request_id
        )


def response_from_message(
    request: ModelRequest,
    message: dict[str, Any],
    latency_seconds: float,
    request_id: str | None,
    batch: bool = False,
) -> ModelResponse:
    """Turn a raw Messages API response into a recorded response."""
    text = "".join(
        block.get("text", "")
        for block in message.get("content", [])
        if block.get("type") == "text"
    )
    usage = message.get("usage") or {}
    answer, error = None, None
    if message.get("stop_reason") == "refusal":
        error = f"refusal: {message.get('stop_details')}"
    else:
        try:
            answer = json.loads(text)
        except json.JSONDecodeError as exc:
            error = f"answer is not JSON: {exc}"
    return ModelResponse(
        request_key=request.key(),
        model=message.get("model", request.model),
        stop_reason=message.get("stop_reason"),
        text=text,
        answer=answer,
        usage=usage,
        cost_usd=cost_usd(request.model, usage, batch),
        latency_seconds=round(latency_seconds, 3),
        request_id=request_id,
        batch=batch,
        error=error,
    )


class RecordingModel:
    """Wraps a model and saves every call under ``directory``."""

    def __init__(self, model: Model, directory: Path) -> None:
        self._model = model
        self._directory = directory
        directory.mkdir(parents=True, exist_ok=True)

    def call(self, request: ModelRequest) -> ModelResponse:
        response = self._model.call(request)
        record = {"request": request.params(), "response": asdict(response)}
        path = self._directory / f"{request.key()}.json"
        path.write_text(
            json.dumps(record, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        return response


class ReplayModel:
    """Answers from recorded calls only; never reaches the network."""

    def __init__(self, directory: Path) -> None:
        self._directory = directory

    def call(self, request: ModelRequest) -> ModelResponse:
        path = self._directory / f"{request.key()}.json"
        if not path.is_file():
            raise MissingRecording(f"no recorded call {path.name}")
        record = json.loads(path.read_text(encoding="utf-8"))
        return ModelResponse(**record["response"])
