import httpx
import pytest


@pytest.fixture(autouse=True)
def block_live_network(monkeypatch: pytest.MonkeyPatch) -> None:
    """Fail any test that reaches a real transport instead of a mock."""

    def refuse(self, request: httpx.Request) -> httpx.Response:
        raise AssertionError(f"live network call attempted: {request.url}")

    monkeypatch.setattr(httpx.HTTPTransport, "handle_request", refuse)
