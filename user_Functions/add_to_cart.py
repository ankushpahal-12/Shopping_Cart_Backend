"""
Add products to cart functionality for users
"""

from Authentication.user_login import validate_user_session
from data.products import products_data
from data.carts import carts_data, Cart
from data.exceptions import ProductNotFoundError, CartError


def add_to_cart(session_id: str, product_id: str, quantity: int):
    """
    Add product to cart (user function)
    
    Args:
        session_id: User's session identifier
        product_id: ID of the product to add
        quantity: Quantity to add
    
    Raises:
        AuthenticationError: If session is invalid
        ProductNotFoundError: If product not found
        CartError: If cart operation fails
    """
    # Validate user session
    user_id = validate_user_session(session_id)
    
    try:
        # Check if product exists
        if product_id not in products_data:
            raise ProductNotFoundError(f"Product with ID {product_id} not found")
        
        product = products_data[product_id]
        if not product.is_active():
            raise ProductNotFoundError(f"Product {product.name} is not available")
        
        # Get or create cart for user
        if user_id not in carts_data:
            carts_data[user_id] = Cart(user_id)
        
        cart = carts_data[user_id]
        cart.add_item(product, quantity)
        
        print(f"Added {quantity} x {product.name} to cart successfully!")
        
    except (ProductNotFoundError, CartError) as e:
        print(f"Error adding to cart: {e}")
        raise