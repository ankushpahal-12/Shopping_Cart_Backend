"""
Delete category functionality for admin
"""

from Authentication.admin_login import validate_admin_session
from data.categories import categories_data
from data.products import products_data
from data.exceptions import CategoryNotFoundError


def delete_category(session_id: str, category_id: str):
    """
    Delete category (admin function)
    
    Args:
        session_id: Admin's session identifier
        category_id: ID of the category to delete
    
    Raises:
        AuthenticationError: If session is invalid
        CategoryNotFoundError: If category doesn't exist or has products
    """
    # Validate admin session
    validate_admin_session(session_id)
    
    try:
        # Check if category exists
        if category_id not in categories_data:
            raise CategoryNotFoundError(f"Category with ID {category_id} not found")
        
        # Check if any products use this category
        products_in_category = [p for p in products_data.values() 
                              if p.category_id == category_id and p.is_active()]
        
        if products_in_category:
            raise CategoryNotFoundError(f"Cannot delete category. {len(products_in_category)} products are using this category")
        
        category = categories_data[category_id]
        category.deactivate()
        
        print(f"Category '{category.name}' deleted successfully!")
        
    except CategoryNotFoundError as e:
        print(f"Error deleting category: {e}")
        raise