"""
Remove products from cart functionality for users
"""

from Authentication.user_login import validate_user_session
from data.carts import carts_data
from data.exceptions import CartError


def remove_from_cart(session_id: str, product_id: str):
    """
    Remove product from cart (user function)
    
    Args:
        session_id: User's session identifier
        product_id: ID of the product to remove
    
    Raises:
        AuthenticationError: If session is invalid
        CartError: If cart operation fails
    """
    # Validate user session
    user_id = validate_user_session(session_id)
    
    try:
        # Check if user has a cart
        if user_id not in carts_data:
            raise CartError("Cart is empty")
        
        cart = carts_data[user_id]
        cart.remove_item(product_id)
        
        print("Product removed from cart successfully!")
        
    except CartError as e:
        print(f"Error removing from cart: {e}")
        raise