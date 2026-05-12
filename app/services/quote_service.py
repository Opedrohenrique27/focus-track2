import logging

import httpx

from app.core.config import settings
from app.schemas.quote import QuoteResponse

logger = logging.getLogger(__name__)

FALLBACK_QUOTES = [
    QuoteResponse(
        quote="The secret of getting ahead is getting started.",
        author="Mark Twain",
    ),
    QuoteResponse(
        quote="It always seems impossible until it's done.",
        author="Nelson Mandela",
    ),
    QuoteResponse(
        quote="Focus on being productive instead of busy.",
        author="Tim Ferriss",
    ),
]


class QuoteService:
    async def get_random_quote(self) -> QuoteResponse:
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(settings.quotes_api_url)
                response.raise_for_status()
                data = response.json()
                if isinstance(data, list) and data:
                    item = data[0]
                    return QuoteResponse(
                        quote=item.get("q", "Keep going."),
                        author=item.get("a", "Unknown"),
                    )
        except Exception as e:
            logger.warning(f"Failed to fetch quote from API: {e}. Using fallback.")

        import random

        return random.choice(FALLBACK_QUOTES)
