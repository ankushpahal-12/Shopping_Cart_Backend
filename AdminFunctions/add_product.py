"""
Add product functionality for admin
"""

from Authentication.admin_login import validate_admin_session
from data.products import products_data, Product
from data.categories import categories_data
from data.exceptions import CategoryNotFoundError


def add_product(session_id: str, name: str, price: float, category_id: str, 
                description: str = "", stock: int = 0):
    """
    Add new product (admin function)
    
    Args:
        session_id: Admin's session identifier
        name: Product name
        price: Product price
        category_id: Category ID for the product
        description: Product description (optional)
        stock: Initial stock quantity (optional)
    
    Returns:
        product_id: ID of the newly created product
    
    Raises:
        AuthenticationError: If session is invalid
        CategoryNotFoundError: If category doesn't exist
        ValueError: If input validation fails
    """
    # Validate admin session
    validate_admin_session(session_id)
    
    try:
        # Check if category exists
        if category_id not in categories_data:
            raise CategoryNotFoundError(f"Category with ID {category_id} not found")
        
        # Generate new product ID
        product_id = f"prod{len(products_data) + 1}"
        
        # Create new product
        product = Product(product_id, name, price, category_id, description, stock)
        products_data[product_id] = product
        
        print(f"Product '{name}' added successfully with ID: {product_id}")
        return product_id
        
    except (CategoryNotFoundError, ValueError) as e:
        print(f"Error adding product: {e}")
        raise