"""
Session management for authentication
"""

import uuid
from typing import Dict, Optional
from data.exceptions import AuthenticationError, AuthorizationError


class Authentication:
    """Handles user and admin authentication"""
    
    def __init__(self):
        self.__user_sessions: Dict[str, str] = {}  # session_id -> user_id
        self.__admin_sessions: Dict[str, str] = {}  # session_id -> admin_id
    
    def login_user(self, users: Dict, username: str, password: str) -> str:
        """Authenticate user and create session"""
        user = None
        for u in users.values():
            if u.username == username:
                user = u
                break
        
        if not user or not user.verify_password(password) or not user.is_active():
            raise AuthenticationError("Invalid username or password")
        
        # Create session
        session_id = str(uuid.uuid4())
        self.__user_sessions[session_id] = user.user_id
        return session_id
    
    def login_admin(self, admins: Dict, username: str, password: str) -> str:
        """Authenticate admin and create session"""
        admin = None
        for a in admins.values():
            if a.username == username:
                admin = a
                break
        
        if not admin or not admin.verify_password(password) or not admin.is_active():
            raise AuthenticationError("Invalid admin credentials")
        
        # Create session
        session_id = str(uuid.uuid4())
        self.__admin_sessions[session_id] = admin.admin_id
        return session_id
    
    def validate_user_session(self, session_id: str) -> Optional[str]:
        """Validate user session and return user ID"""
        return self.__user_sessions.get(session_id)
    
    def validate_admin_session(self, session_id: str) -> Optional[str]:
        """Validate admin session and return admin ID"""
        return self.__admin_sessions.get(session_id)
    
    def logout_user(self, session_id: str):
        """Logout user by removing session"""
        if session_id in self.__user_sessions:
            del self.__user_sessions[session_id]
    
    def logout_admin(self, session_id: str):
        """Logout admin by removing session"""
        if session_id in self.__admin_sessions:
            del self.__admin_sessions[session_id]


# Global authentication instance
auth_manager = Authentication()