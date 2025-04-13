"""
API client for interacting with the Cat Facts API.
"""

import logging
from typing import Dict, Optional, Any

import requests

from config.config import (
    BASE_URL,
    DEFAULT_TIMEOUT,
    DEFAULT_HEADERS,
    DEFAULT_LIMIT,
    DEFAULT_PAGE,
)
from api.endpoints import (
    RANDOM_FACT_ENDPOINT,
    FACTS_LIST_ENDPOINT,
)

logger = logging.getLogger(__name__)


class CatFactsClient:
    """
    Client for interacting with the Cat Facts API.
    """

    def __init__(
        self,
        base_url: str = BASE_URL,
        timeout: int = DEFAULT_TIMEOUT,
        headers: Dict[str, str] = None,
    ):
        """
        Initialize the Cat Facts API client.
        """
        self.base_url = base_url
        self.timeout = timeout
        self.headers = headers or DEFAULT_HEADERS.copy()
        logger.debug(f"Initialized CatFactsClient with base_url: {base_url}")

    def get_random_fact(self) -> requests.Response:
        """
        Get a random cat fact.
        """
        return self.get(RANDOM_FACT_ENDPOINT)

    def get_facts(
        self, limit: int = DEFAULT_LIMIT, page: int = DEFAULT_PAGE
    ) -> requests.Response:
        """
        Get a paginated list of cat facts.
        """
        params = {"limit": limit, "page": page}
        return self.get(FACTS_LIST_ENDPOINT, params=params)

    def get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        """
        Send a GET request to the specified endpoint.
        """
        url = f"{self.base_url}{endpoint}"
        logger.debug(f"Making GET request to {url} with params: {params}")
        
        try:
            response = requests.get(
                url, params=params, headers=self.headers, timeout=self.timeout
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Error making request to {url}: {str(e)}")
            raise

    def post(
        self, endpoint: str, data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        """
        Send a POST request to the specified endpoint.
        """
        url = f"{self.base_url}{endpoint}"
        logger.debug(f"Making POST request to {url} with data: {data}")
        
        try:
            response = requests.post(
                url, json=data, params=params, headers=self.headers, timeout=self.timeout
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Error making request to {url}: {str(e)}")
            raise
