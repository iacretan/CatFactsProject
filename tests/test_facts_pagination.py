import pytest


def test_facts_custom_limit(cat_facts_client):
    """Test getting facts with a custom limit."""
    limit = 3
    
    response = cat_facts_client.get_facts(limit=limit)
    
    assert response.status_code == 200
    
    response_data = response.json()
    assert "data" in response_data
    assert len(response_data["data"]) == limit


def test_facts_pagination_page(cat_facts_client):
    """Test getting a specific page of facts."""
    page = 2
    
    response = cat_facts_client.get_facts(page=page)
    
    assert response.status_code == 200
    
    response_data = response.json()
    assert response_data["current_page"] == page
