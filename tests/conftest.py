"""
Pytest fixtures for the Cat Facts API tests.
"""

import pytest

from api.client import CatFactsClient


@pytest.fixture
def cat_facts_client():
    """
    Fixture that provides a configured CatFactsClient instance.
    """
    client = CatFactsClient()
    yield client
