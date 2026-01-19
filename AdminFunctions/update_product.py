"""
Update product functionality for admin
"""

from Authentication.admin_login import validate_admin_session
from data.products import products_data
from data.exceptions import ProductNotFoundError


def update_product(session_id: str, product_id: str, name: str = None, 
                  price: float = None, description: str = None, stock: int = None):
    """
    Update existing product (admin function)
    
    Args:
        session_id: Admin's session identifier
        product_id: ID of the product to update
        name: New product name (optional)
        price: New product price (optional)
        description: New product description (optional)
        stock: New stock quantity (optional)
    
    Raises:
        AuthenticationError: If session is invalid
        ProductNotFoundError: If product doesn't exist
        ValueError: If input validation fails
    """
    # Validate admin session
    validate_admin_session(session_id)
    
    try:
        # Check if product exists
        if product_id not in products_data:
            raise ProductNotFoundError(f"Product with ID {product_id} not found")
        
        product = products_data[product_id]
        
        # Update product attributes if provided
        if name is not None:
            product.name = name
        if price is not None:
            product.price = price
        if description is not None:
            product.description = description
        if stock is not None:
            product.stock = stock
        
        print(f"Product '{product.name}' updated successfully!")
        
    except (ProductNotFoundError, ValueError) as e:
        print(f"Error updating product: {e}")
        raise