import httpx
import httpx2
import pytest


@pytest.fixture(autouse=True)
def block_live_network(monkeypatch: pytest.MonkeyPatch) -> None:
    """Fail any test that reaches a real transport instead of a mock.

    Acquisition uses ``httpx``; the Anthropic SDK uses ``httpx2``. Both are
    blocked, sync and async, so no test can call a source or a model.
    """

    def refuse(self, request) -> None:
        raise AssertionError(f"live network call attempted: {request.url}")

    async def refuse_async(self, request) -> None:
        raise AssertionError(f"live network call attempted: {request.url}")

    for module in (httpx, httpx2):
        monkeypatch.setattr(module.HTTPTransport, "handle_request", refuse)
        monkeypatch.setattr(
            module.AsyncHTTPTransport, "handle_async_request", refuse_async
        )
