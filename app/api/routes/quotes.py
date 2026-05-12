from fastapi import APIRouter

from app.schemas.quote import QuoteResponse
from app.services.quote_service import QuoteService

router = APIRouter(prefix="/quotes", tags=["Quotes"])


@router.get("/random", response_model=QuoteResponse)
async def get_random_quote():
    """Get a random motivational quote."""
    service = QuoteService()
    return await service.get_random_quote()
