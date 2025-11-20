"""Unit tests for main module functions and classes.

This module demonstrates various pytest features including:
- Basic assertions
- Exception testing
- Fixtures for setup/teardown
- Parametrized tests
"""

from main import weather, add, divide, UserManager, DataBase
import pytest

# ========== COMMENTED OUT TESTS - Examples of Basic Testing ==========
# These tests demonstrate fundamental pytest concepts

# def test_weather():
#     """Test weather classification function."""
#     assert weather(21) == "Cold"

# def test_add():
#     """Test addition function with multiple assertions."""
#     assert add(1,5) == 6, "1+5=6"
#     assert add(6,4) == 10, "6+4=10"
#     assert add(8,3) == 11, "8+3=11"
#     assert add(5,-1) == 5, "5-1=4"


# def test_divide():
#     """Test that divide function raises ValueError for division by zero."""
#     with pytest.raises(ValueError, match="Can divide by zero"):
#          divide(10,0)

# ========== COMMENTED OUT TESTS - Fixture Examples ==========
# These tests demonstrate pytest fixtures for setup and dependency injection

# @pytest.fixture
# def usermanager():
#     """Fixture that provides a fresh UserManager instance for each test."""
#     return UserManager()

# def test_add_user(usermanager):
#     """Test adding a new user and retrieving their email."""
#     assert usermanager.add_user("john","john@gmail.com") == True
#     assert usermanager.get_user("john") == "john@gmail.com"

# def test_duplicate_user(usermanager):
#     """Test that adding a duplicate user raises ValueError."""
#     usermanager.add_user("john","john@gmail.com")
#     with pytest.raises(ValueError):
#         usermanager.add_user("john","john@gmail.com")


# @pytest.fixture
# def db():
#     """Fixture that provides a DataBase instance with cleanup after test.
#     
#     The yield statement allows teardown code to run after the test completes.
#     """
#     database = DataBase()
#     yield database
#     # Teardown: clear database after test
#     database.data.clear()


# def test_add_users(db):
#     """Test adding a user to the database."""
#     db.add_users("john","john@gmail.com")
#     assert db.get_users("john") == "john@gmail.com"

# def test_delete_user(db):
#     """Test deleting a user from the database."""
#     db.add_users("john","bob")
#     db.delete_users("john")
#     assert db.get_users("john") is None

# ========== ACTIVE TESTS - Parametrized Testing ==========

@pytest.mark.parametrize("num1,num2,expected", [
    (1, 5, 6),    # Test case 1: positive numbers
    (6, 4, 10),   # Test case 2: positive numbers
    (8, 3, 11),   # Test case 3: positive numbers
    (5, -1, 4),   # Test case 4: positive and negative number
])
def test_add(num1, num2, expected):
    """Parametrized test for the add function.
    
    This test runs 4 times with different input combinations.
    Demonstrates pytest.mark.parametrize for reducing test code duplication.
    
    Args:
        num1 (int): First number to add.
        num2 (int): Second number to add.
        expected (int): Expected sum of num1 and num2.
    """
    # Note: The following assertions are redundant (repeated 4 times)
    # Typically, only one assertion is needed per parametrized test
    assert add(num1, num2) == expected
    assert add(num1, num2) == expected
    assert add(num1, num2) == expected
    assert add(num1, num2) == expected