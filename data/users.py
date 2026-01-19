"""
User class and user data management
"""

class User:
    """Represents a user in the shopping system"""
    
    def __init__(self, user_id: str, username: str, password: str, email: str):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__email = email
        self.__is_active = True
    
    @property
    def user_id(self) -> str:
        return self.__user_id
    
    @property
    def username(self) -> str:
        return self.__username
    
    @property
    def email(self) -> str:
        return self.__email
    
    def verify_password(self, password: str) -> bool:
        """Verify user password"""
        return self.__password == password
    
    def is_active(self) -> bool:
        """Check if user account is active"""
        return self.__is_active
    
    def __str__(self) -> str:
        return f"User(id={self.__user_id}, username={self.__username})"


# Demo users data
users_data = {
    "user1": User("user1", "john_doe", "password123", "john@email.com"),
    "user2": User("user2", "jane_smith", "password456", "jane@email.com")
}