# Cat Facts API Testing Framework

A reusable testing framework for the Cat Facts API (https://alexwohlbruck.github.io/cat-facts/).

## Features

- Modular API client for making requests to the Cat Facts API
- Pytest-based test structure
- Validation utilities for response verification
- Easy to extend for additional test cases

## Requirements

- Python 3.8+
- Poetry for dependency management

## Installation

1. Clone this repository
2. Install dependencies using Poetry:

```bash
poetry install
```

## Running Tests

Run all tests:

```bash
poetry run pytest
```

Run with HTML report:

```bash
poetry run pytest --html=report.html
```

Run specific test file:

```bash
poetry run pytest tests/test_random_fact.py
```

## Test Cases

### Test Case 1: Get a random cat fact

- Sends a GET request to `/fact`
- Validates status code is 200
- Asserts that "fact" is a non-empty string and "length" matches the length of the fact

### Test Case 2: Get a paginated list of facts

- Sends a GET request to `/facts?limit=5`
- Validates status code is 200
- Ensures data returns 5 facts, each with fact and length
- Validates pagination metadata is present (per_page, total, etc.)

## Project Structure

```
cat_facts_api_tests/
├── pyproject.toml         # Poetry configuration and dependencies
├── README.md              # Project documentation
├── cat_facts_api/         # Main package
│   ├── api/               # API client module
│   │   └── client.py      # API client implementation
│   ├── config/            # Configuration module
│   │   └── settings.py    # Environment and configuration settings
│   └── utils/             # Utility functions
│       └── validators.py  # Response validation helpers
└── tests/                 # Test directory
    ├── conftest.py        # pytest fixtures and configuration
    ├── test_random_fact.py  # Test Case 1 implementation
    └── test_facts_list.py   # Test Case 2 implementation
