# Cat Facts API Testing Framework

A reusable testing framework for the Cat Facts API (https://alexwohlbruck.github.io/cat-facts/).

## Project Structure

```
CatFactsProject/
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore file
├── poetry.lock            # Poetry lock file
├── pyproject.toml         # Poetry configuration and dependencies
├── README.md              # Project documentation
├── api/                   # API client module
│   ├── __init__.py
│   ├── client.py          # API client implementation
│   └── endpoints.py       # API endpoints definitions
├── config/                # Configuration module
│   ├── __init__.py
│   └── config.py          # Environment and configuration settings
└── tests/                 # Test directory
    ├── __init__.py
    ├── conftest.py        # pytest fixtures and configuration
    ├── test_fact_validation.py  # Fact validation tests
    ├── test_facts_list.py       # Facts list tests
    ├── test_facts_pagination.py # Pagination tests
    └── test_random_fact.py      # Random fact tests
```

## Features

- Modular API client for making requests to the Cat Facts API
- Pytest-based test structure
- Validation utilities for response verification
- Easy to extend for additional test cases

## Requirements

- Python 3.10+
- Poetry for dependency management

## Installation

1. Clone this repository
2. Create a `.env` file based on the `.env.example` template
3. Install dependencies using Poetry:

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

### Test Case 3: Fact validation

- Validates the structure and content of fact responses
- Ensures all required fields are present and correctly formatted

### Test Case 4: Facts pagination

- Tests the pagination functionality of the facts endpoint
- Verifies correct behavior with different page and limit parameters


## Test Results

![Test Results](Screenshot%202025-04-13%20214054.png)
