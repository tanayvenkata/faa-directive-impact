"""Per-token prices used to report what each recorded call cost.

Prices are U.S. dollars per million tokens from Anthropic's published table,
as of 2026-10-06. They are for reporting only; the bill is the authority. A
5-minute cache write costs 1.25x the input price. The Batch API halves every
price. The Claude Haiku 5.5 cache-read price is assumed at 0.1x input, the
usual ratio; the published table did not list it. Claude Haiku 5.5's prices
apply to prompts up to 100,000 tokens; a longer prompt (cached tokens
included) is billed at five times every rate.
"""

from dataclasses import dataclass
from typing import Any

PRICES_AS_OF = "2026-10-06"
CACHE_WRITE_MULTIPLIER = 1.25
BATCH_MULTIPLIER = 0.5


@dataclass(frozen=True)
class ModelPrice:
    input: float
    output: float
    cache_read: float
    long_prompt_tokens: int | None = None
    long_prompt_multiplier: float = 1.0


PRICES = {
    "claude-haiku-5-5": ModelPrice(
        input=0.10,
        output=0.50,
        cache_read=0.01,
        long_prompt_tokens=100_000,
        long_prompt_multiplier=5.0,
    ),
    "claude-sonnet-5-5": ModelPrice(input=2.00, output=10.00, cache_read=0.20),
    "claude-opus-5-5": ModelPrice(input=4.00, output=20.00, cache_read=0.20),
}


def cost_usd(model: str, usage: dict[str, Any], batch: bool = False) -> float:
    """Return the cost of one call from its usage counts."""
    price = PRICES[model]
    dollars = (
        usage.get("input_tokens", 0) * price.input
        + (usage.get("cache_creation_input_tokens") or 0)
        * price.input
        * CACHE_WRITE_MULTIPLIER
        + (usage.get("cache_read_input_tokens") or 0) * price.cache_read
        + usage.get("output_tokens", 0) * price.output
    ) / 1_000_000
    prompt_tokens = (
        usage.get("input_tokens", 0)
        + (usage.get("cache_creation_input_tokens") or 0)
        + (usage.get("cache_read_input_tokens") or 0)
    )
    if price.long_prompt_tokens and prompt_tokens > price.long_prompt_tokens:
        dollars *= price.long_prompt_multiplier
    return round(dollars * (BATCH_MULTIPLIER if batch else 1.0), 6)
