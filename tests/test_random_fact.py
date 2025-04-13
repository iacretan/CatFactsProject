import pytest


def test_get_random_fact(cat_facts_client):
    response = cat_facts_client.get_random_fact()
    
    assert response.status_code == 200
    
    fact_data = response.json()
    assert "fact" in fact_data
    assert "length" in fact_data
    assert len(fact_data["fact"]) > 0
