import pytest


def test_get_facts_list_pagination(cat_facts_client):
    limit = 5
    
    response = cat_facts_client.get_facts(limit=limit)
    
    assert response.status_code == 200
    
    response_data = response.json()
    assert "data" in response_data
    assert len(response_data["data"]) == limit
