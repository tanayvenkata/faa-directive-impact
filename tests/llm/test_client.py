import json
from pathlib import Path

import anthropic
import pytest

from faa_directive_impact.llm.client import (
    LiveModel,
    MissingRecording,
    ModelRequest,
    RecordingModel,
    ReplayModel,
    call_batch,
)
from faa_directive_impact.llm.pricing import cost_usd

SCHEMA = {
    "type": "object",
    "properties": {"applies": {"type": "boolean"}},
    "required": ["applies"],
    "additionalProperties": False,
}


def request(question: str = "Does it apply?") -> ModelRequest:
    return ModelRequest(
        model="claude-sonnet-5-5",
        instructions="Screen the engine.",
        document="AD text",
        question=question,
        output_schema=SCHEMA,
    )


class FakeMessage:
    def __init__(self, payload: dict) -> None:
        self._payload = payload
        self._request_id = "req_test"

    def to_dict(self) -> dict:
        return self._payload


class FakeClient:
    """Stands in for anthropic.Anthropic; records what it was sent."""

    def __init__(self, payload: dict) -> None:
        self.sent: list[dict] = []
        self.messages = self
        self._payload = payload

    def create(self, **params):
        self.sent.append(params)
        return FakeMessage(self._payload)


def payload(text: str, stop_reason: str = "end_turn") -> dict:
    return {
        "model": "claude-sonnet-5-5",
        "stop_reason": stop_reason,
        "content": [
            {"type": "thinking", "thinking": ""},
            {"type": "text", "text": text},
        ],
        "usage": {
            "input_tokens": 100,
            "output_tokens": 50,
            "cache_creation_input_tokens": 0,
            "cache_read_input_tokens": 4000,
        },
    }


def test_document_is_the_cache_breakpoint_and_question_follows_it() -> None:
    params = request().params()

    assert "cache_control" not in params["system"][0]
    assert params["system"][1]["cache_control"] == {"type": "ephemeral"}
    assert params["messages"] == [{"role": "user", "content": "Does it apply?"}]
    assert params["output_config"]["format"]["schema"] == SCHEMA
    assert params["output_config"]["effort"] == "medium"


def test_request_key_is_stable_and_tracks_every_input() -> None:
    assert request().key() == request().key()
    assert request().key() != request("Another engine?").key()


def test_live_model_parses_structured_answer_and_costs_it() -> None:
    client = FakeClient(payload('{"applies": true}'))

    response = LiveModel(client).call(request())

    assert client.sent == [request().params()]
    assert response.answer == {"applies": True}
    assert response.error is None
    assert response.request_id == "req_test"
    assert response.cost_usd == cost_usd("claude-sonnet-5-5", payload("")["usage"])


def test_refusal_is_recorded_as_a_result_not_an_answer() -> None:
    response = LiveModel(FakeClient(payload("", "refusal"))).call(request())

    assert response.answer is None
    assert response.error.startswith("refusal")


def test_non_json_answer_is_recorded_as_an_error() -> None:
    response = LiveModel(FakeClient(payload("yes"))).call(request())

    assert response.answer is None
    assert "not JSON" in response.error


def test_recorded_calls_replay_without_the_model(tmp_path: Path) -> None:
    live = RecordingModel(
        LiveModel(FakeClient(payload('{"applies": false}'))), tmp_path
    )
    original = live.call(request())

    replayed = ReplayModel(tmp_path).call(request())

    assert replayed == original
    record = json.loads((tmp_path / f"{request().key()}.json").read_text())
    assert record["request"] == request().params()


def test_replay_refuses_a_call_that_was_never_recorded(tmp_path: Path) -> None:
    with pytest.raises(MissingRecording):
        ReplayModel(tmp_path).call(request())


def test_cost_counts_cache_writes_reads_and_batch_discount() -> None:
    usage = {
        "input_tokens": 1_000_000,
        "output_tokens": 1_000_000,
        "cache_creation_input_tokens": 1_000_000,
        "cache_read_input_tokens": 1_000_000,
    }

    assert cost_usd("claude-sonnet-5-5", usage) == 2.00 + 10.00 + 2.50 + 0.20
    assert cost_usd("claude-sonnet-5-5", usage, batch=True) == 7.35


def test_sdk_cannot_reach_the_network_during_tests() -> None:
    client = anthropic.Anthropic(api_key="test-key", max_retries=0)

    with pytest.raises(anthropic.APIConnectionError) as raised:
        LiveModel(client).call(request())

    causes = []
    error: BaseException | None = raised.value
    while error is not None:
        causes.append(str(error))
        error = error.__cause__ or error.__context__
    assert any("live network call attempted" in cause for cause in causes)


class FakeBatches:
    def __init__(self, text: str) -> None:
        self.created = []
        self._text = text
        self.polls = 0

    def create(self, requests):
        self.created = requests
        return type("Batch", (), {"id": "batch_1"})()

    def retrieve(self, batch_id):
        self.polls += 1
        status = "ended" if self.polls > 1 else "in_progress"
        return type("Status", (), {"processing_status": status})()

    def results(self, batch_id):
        for item in self.created:
            result = type(
                "Result",
                (),
                {"type": "succeeded", "message": FakeMessage(payload(self._text))},
            )()
            yield type("Item", (), {"custom_id": item["custom_id"], "result": result})()


def test_batch_runs_at_half_price_and_keys_results_by_request() -> None:
    batches = FakeBatches('{"applies": true}')
    client = type("Client", (), {"messages": type("M", (), {"batches": batches})()})()
    requests = [request("one?"), request("two?")]

    responses = call_batch(client, requests, sleep=lambda _: None)

    assert set(responses) == {r.key() for r in requests}
    assert [item["params"] for item in batches.created] == [
        r.params() for r in requests
    ]
    response = responses[requests[0].key()]
    assert response.batch is True
    assert response.answer == {"applies": True}
    assert response.cost_usd == cost_usd(
        "claude-sonnet-5-5", payload("")["usage"], batch=True
    )


def test_haiku_prompts_over_100k_tokens_cost_five_times_more() -> None:
    short = {"input_tokens": 90_000, "output_tokens": 1_000}
    long = {"input_tokens": 1_000, "cache_read_input_tokens": 100_000,
            "output_tokens": 1_000}  # fmt: skip

    assert cost_usd("claude-haiku-5-5", short) == round(
        (90_000 * 0.10 + 1_000 * 0.50) / 1_000_000, 6
    )
    assert cost_usd("claude-haiku-5-5", long) == round(
        5 * (1_000 * 0.10 + 100_000 * 0.01 + 1_000 * 0.50) / 1_000_000, 6
    )
