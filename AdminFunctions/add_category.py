"""
Add category functionality for admin
"""

from Authentication.admin_login import validate_admin_session
from data.categories import categories_data, Category


def add_category(session_id: str, name: str, description: str = ""):
    """
    Add new category (admin function)
    
    Args:
        session_id: Admin's session identifier
        name: Category name
        description: Category description (optional)
    
    Returns:
        category_id: ID of the newly created category
    
    Raises:
        AuthenticationError: If session is invalid
        ValueError: If input validation fails
    """
    # Validate admin session
    validate_admin_session(session_id)
    
    try:
        # Generate new category ID
        category_id = f"cat{len(categories_data) + 1}"
        
        # Create new category
        category = Category(category_id, name, description)
        categories_data[category_id] = category
        
        print(f"Category '{name}' added successfully with ID: {category_id}")
        return category_id
        
    except ValueError as e:
        print(f"Error adding category: {e}")
        raise
