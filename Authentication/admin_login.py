"""
Admin login functionality
"""

from data.admin import admin_data
from data.sessions import auth_manager
from data.exceptions import AuthenticationError


def admin_login(username: str, password: str) -> str:
    """
    Authenticate admin and create session
    
    Args:
        username: Admin's username
        password: Admin's password
    
    Returns:
        session_id: Unique session identifier
    
    Raises:
        AuthenticationError: If login fails
    """
    try:
        session_id = auth_manager.login_admin(admin_data, username, password)
        print(f"Welcome Admin {username}! Login successful.")
        return session_id
    except AuthenticationError as e:
        print(f"Admin login failed: {e}")
        raise


def validate_admin_session(session_id: str) -> str:
    """
    Validate admin session and return admin ID
    
    Args:
        session_id: Session identifier to validate
    
    Returns:
        admin_id: Admin identifier if session is valid
    
    Raises:
        AuthenticationError: If session is invalid
    """
    admin_id = auth_manager.validate_admin_session(session_id)
    if not admin_id:
        raise AuthenticationError("Invalid or expired admin session")
    return admin_id


def admin_logout(session_id: str):
    """
    Logout admin by removing session
    
    Args:
        session_id: Session identifier to logout
    """
    auth_manager.logout_admin(session_id)
    print("Admin logged out successfully!")
