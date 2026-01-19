"""
Delete product functionality for admin
"""

from Authentication.admin_login import validate_admin_session
from data.products import products_data
from data.exceptions import ProductNotFoundError


def delete_product(session_id: str, product_id: str):
    """
    Delete product (admin function)
    
    Args:
        session_id: Admin's session identifier
        product_id: ID of the product to delete
    
    Raises:
        AuthenticationError: If session is invalid
        ProductNotFoundError: If product doesn't exist
    """
    # Validate admin session
    validate_admin_session(session_id)
    
    try:
        # Check if product exists
        if product_id not in products_data:
            raise ProductNotFoundError(f"Product with ID {product_id} not found")
        
        product = products_data[product_id]
        product.deactivate()
        
        print(f"Product '{product.name}' deleted successfully!")
        
    except ProductNotFoundError as e:
        print(f"Error deleting product: {e}")
        raise