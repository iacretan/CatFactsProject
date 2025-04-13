"""
Configuration settings for the Cat Facts API testing framework.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base URL for the Cat Facts API
BASE_URL = os.getenv("BASE_URL")

# Default timeout for API requests (in seconds)
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", 10))

# Default headers for API requests
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Default pagination settings
DEFAULT_LIMIT = 5
DEFAULT_PAGE = 1
