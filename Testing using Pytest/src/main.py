"""Main module containing utility functions and classes for testing demonstrations."""

def weather(temperature):
    """Classify weather based on temperature.
    
    Args:
        temperature (int/float): The temperature value to classify.
        
    Returns:
        str: "Hot" if temperature > 20, "Cold" otherwise.
    """
    if temperature > 20:
        return "Hot"
    else:
        return "Cold"

def add(a, b):
    """Add two numbers together.
    
    Args:
        a (int/float): First number.
        b (int/float): Second number.
        
    Returns:
        int/float: Sum of a and b.
    """
    return a + b

def divide(a, b):
    """Divide two numbers with zero-division protection.
    
    Args:
        a (int/float): Numerator.
        b (int/float): Denominator.
        
    Returns:
        float: Result of a divided by b.
        
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b

class UserManager:
    """Manages user accounts with username-email mapping."""
    
    def __init__(self):
        """Initialize an empty user dictionary."""
        self.users = {}

    def add_user(self, username, email):
        """Add a new user to the system.
        
        Args:
            username (str): Unique username for the user.
            email (str): Email address of the user.
            
        Returns:
            bool: True if user was successfully added.
            
        Raises:
            ValueError: If username already exists.
        """
        if username in self.users:
            raise ValueError("User already exists") 
        self.users[username] = email
        return True
    
    def get_user(self, username):
        """Retrieve a user's email by username.
        
        Args:
            username (str): The username to lookup.
            
        Returns:
            str or None: User's email if found, None otherwise.
        """
        return self.users.get(username)
    
class DataBase:
    """Simple in-memory database for user management."""
    
    def __init__(self):
        """Initialize an empty database dictionary."""
        self.data = {}

    def add_users(self, user_id, email):
        """Add a new user to the database.
        
        Args:
            user_id (str): Unique identifier for the user.
            email (str): Email address of the user.
            
        Raises:
            ValueError: If user_id already exists in database.
        """
        if user_id in self.data:
            raise ValueError("User already exists")
        self.data[user_id] = email

    def get_users(self, user_id):
        """Retrieve a user's email by user_id.
        
        Args:
            user_id (str): The user_id to lookup.
            
        Returns:
            str or None: User's email if found, None otherwise.
        """
        return self.data.get(user_id, None)
    
    def delete_users(self, user_id):
        """Delete a user from the database.
        
        Args:
            user_id (str): The user_id to delete.
        """
        if user_id in self.data:
            del self.data[user_id]
