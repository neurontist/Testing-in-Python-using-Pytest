# Testing with Pytest

A comprehensive demonstration of unit testing and integration testing in Python using the pytest framework. This project showcases various testing patterns, best practices, and pytest features.

## 📋 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Test Descriptions](#test-descriptions)
- [Pytest Features Demonstrated](#pytest-features-demonstrated)
- [Requirements](#requirements)

## 🎯 Overview

This project demonstrates professional testing practices in Python, including:

- **Unit Testing**: Testing individual functions and classes in isolation
- **Integration Testing**: Testing REST API endpoints end-to-end
- **Pytest Features**: Fixtures, parametrized tests, exception testing, and mocking capabilities

## 📁 Project Structure

```
Testing using Pytest/
├── main.py              # Main application code with utility functions and classes
├── test_main.py         # Unit tests for main.py
├── test_todo_api.py     # Integration tests for TODO REST API
├── pyproject.toml       # Project configuration and dependencies
└── README.md            # This file
```

## ✨ Features

### Main Application (`main.py`)

- **Weather Classification**: Simple temperature-based weather determination
- **Mathematical Operations**: Addition and division with error handling
- **User Management**: In-memory user storage with username-email mapping
- **Database Simulation**: Simple CRUD operations for user data

### Unit Tests (`test_main.py`)

- Basic function testing with assertions
- Exception handling verification
- Pytest fixtures for setup/teardown
- Parametrized tests to reduce code duplication

### Integration Tests (`test_todo_api.py`)

- REST API endpoint testing
- CRUD operations (Create, Read, Update, Delete)
- Task list management
- Real-world API interaction with https://todo.pixegami.io

## 🚀 Installation

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)

### Setup

1. Clone or download this repository

2. Install dependencies:

   ```powershell
   pip install pytest pytest-mock requests
   ```

   Or using the pyproject.toml:

   ```powershell
   pip install -e .
   ```

## 🧪 Running Tests

### Run All Tests

```powershell
pytest
```

### Run Specific Test File

```powershell
# Run only unit tests
pytest test_main.py

# Run only API integration tests
pytest test_todo_api.py
```

### Run with Verbose Output

```powershell
pytest -v
```

### Run with Test Coverage

```powershell
pytest --cov=main
```

### Run Specific Test Function

```powershell
pytest test_main.py::test_add
pytest test_todo_api.py::test_can_create_task
```

### Run Tests Matching a Pattern

```powershell
pytest -k "add"        # Runs all tests with 'add' in the name
pytest -k "create"     # Runs all tests with 'create' in the name
```

## 📝 Test Descriptions

### Unit Tests (`test_main.py`)

#### Active Tests

- **`test_add`**: Parametrized test that validates the addition function with multiple input combinations:
  - Positive numbers
  - Mixed positive and negative numbers
  - Edge cases

#### Commented Examples (For Learning)

The file includes commented-out examples demonstrating:

- Basic weather classification testing
- Division by zero exception testing
- Fixture usage for UserManager
- Fixture with teardown for DataBase
- Duplicate user validation

### Integration Tests (`test_todo_api.py`)

- **`test_can_call_endpoint`**: Verifies API server is reachable
- **`test_can_create_task`**: Tests task creation and retrieval
- **`test_can_update_task`**: Tests updating task content and completion status
- **`test_can_list_tasks`**: Tests retrieving multiple tasks for a user
- **`test_can_delete_task`**: Tests task deletion and verifies it no longer exists

## 🎓 Pytest Features Demonstrated

### 1. Basic Assertions

```python
assert add(1, 5) == 6
assert weather(25) == "Hot"
```

### 2. Exception Testing

```python
with pytest.raises(ValueError, match="Cannot divide by zero"):
    divide(10, 0)
```

### 3. Fixtures

```python
@pytest.fixture
def db():
    database = DataBase()
    yield database
    database.data.clear()  # Teardown
```

### 4. Parametrized Tests

```python
@pytest.mark.parametrize("num1,num2,expected", [
    (1, 5, 6),
    (6, 4, 10),
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected
```

### 5. Integration Testing

- Real HTTP requests using the `requests` library
- API endpoint testing with assertions on status codes and response data
- UUID-based test data generation to avoid conflicts

## 📦 Requirements

See `pyproject.toml` for full dependency list:

- **pytest** (>=9.0.1): Testing framework
- **pytest-mock** (>=3.15.1): Mocking support for pytest
- **requests**: HTTP library for API testing (install separately)

## 💡 Tips for Using This Project

1. **Start with Unit Tests**: Review `test_main.py` to understand basic pytest concepts
2. **Explore Fixtures**: Uncomment the fixture examples to see setup/teardown in action
3. **Try Parametrized Tests**: Modify the `test_add` parameters to add more test cases
4. **API Testing**: Run `test_todo_api.py` to see integration testing in action
5. **Add Your Own Tests**: Practice by adding tests for edge cases and new functionality

## 🤝 Contributing

This is a learning project. Feel free to:

- Add more test cases
- Implement additional pytest features
- Add new functions to test
- Improve documentation

## 📄 License

This project is for educational purposes.

## 📧 Contact

For questions or suggestions about this testing demonstration, please open an issue or submit a pull request.

---

**Happy Testing!** 🧪✨
