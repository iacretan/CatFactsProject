import pytest


def test_fact_length_validation(cat_facts_client):
    """Test that the length field matches the actual length of the fact."""
    response = cat_facts_client.get_random_fact()
    
    assert response.status_code == 200
    
    fact_data = response.json()
    assert len(fact_data["fact"]) == fact_data["length"]
