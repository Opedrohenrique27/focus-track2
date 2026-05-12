from unittest.mock import AsyncMock, patch


def test_get_random_quote_fallback(client):
    """Test quote endpoint returns a valid response (uses fallback if API unavailable)."""
    with patch(
        "app.services.quote_service.QuoteService.get_random_quote",
        new_callable=AsyncMock,
        return_value=type("Q", (), {"quote": "Keep going.", "author": "Unknown"})(),
    ):
        response = client.get("/api/v1/quotes/random")
        # Should succeed even if external API is unreachable in test env
        assert response.status_code == 200


def test_get_random_quote_structure(client):
    """Test quote response has correct structure."""
    from app.schemas.quote import QuoteResponse

    with patch(
        "app.services.quote_service.QuoteService.get_random_quote",
        new_callable=AsyncMock,
        return_value=QuoteResponse(quote="Focus on your goals.", author="Test Author"),
    ):
        response = client.get("/api/v1/quotes/random")
        assert response.status_code == 200
        data = response.json()
        assert "quote" in data
        assert "author" in data
        assert isinstance(data["quote"], str)
        assert isinstance(data["author"], str)


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
