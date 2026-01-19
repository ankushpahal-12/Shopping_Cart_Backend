"""
Admin class and admin data management
"""

class Admin:
    """Represents an admin user with elevated privileges"""
    
    def __init__(self, admin_id: str, username: str, password: str, email: str):
        self.__admin_id = admin_id
        self.__username = username
        self.__password = password
        self.__email = email
        self.__is_active = True
    
    @property
    def admin_id(self) -> str:
        return self.__admin_id
    
    @property
    def username(self) -> str:
        return self.__username
    
    @property
    def email(self) -> str:
        return self.__email
    
    def verify_password(self, password: str) -> bool:
        """Verify admin password"""
        return self.__password == password
    
    def is_active(self) -> bool:
        """Check if admin account is active"""
        return self.__is_active
    
    def __str__(self) -> str:
        return f"Admin(id={self.__admin_id}, username={self.__username})"


# Demo admin data
admin_data = {
    "admin1": Admin("admin1", "admin", "admin123", "admin@email.com")
}
    "admin1": Admin("admin1", "admin", "admin123", "admin@email.com")
}
