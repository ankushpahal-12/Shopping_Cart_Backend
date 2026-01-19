"""
User login functionality
"""

from data.users import users_data
from data.sessions import auth_manager
from data.exceptions import AuthenticationError


def user_login(username: str, password: str) -> str:
    """
    Authenticate user and create session
    
    Args:
        username: User's username
        password: User's password
    
    Returns:
        session_id: Unique session identifier
    
    Raises:
        AuthenticationError: If login fails
    """
    try:
        session_id = auth_manager.login_user(users_data, username, password)
        print(f"Welcome {username}! Login successful.")
        return session_id
    except AuthenticationError as e:
        print(f"Login failed: {e}")
        raise


def validate_user_session(session_id: str) -> str:
    """
    Validate user session and return user ID
    
    Args:
        session_id: Session identifier to validate
    
    Returns:
        user_id: User identifier if session is valid
    
    Raises:
        AuthenticationError: If session is invalid
    """
    user_id = auth_manager.validate_user_session(session_id)
    if not user_id:
        raise AuthenticationError("Invalid or expired session")
    return user_id


def user_logout(session_id: str):
    """
    Logout user by removing session
    
    Args:
        session_id: Session identifier to logout
    """
    auth_manager.logout_user(session_id)
    print("User logged out successfully!")