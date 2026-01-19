"""
View cart contents functionality for users
"""

from Authentication.user_login import validate_user_session
from data.carts import carts_data


def view_cart(session_id: str):
    """
    View cart contents (user function)
    
    Args:
        session_id: User's session identifier
    
    Raises:
        AuthenticationError: If session is invalid
    """
    # Validate user session
    user_id = validate_user_session(session_id)
    
    # Check if user has items in cart
    if user_id not in carts_data or carts_data[user_id].is_empty():
        print("Your cart is empty.")
        return
    
    cart = carts_data[user_id]
    items = cart.get_items()
    
    print("\n=== Your Cart ===")
    total_amount = 0
    
    for item in items:
        item_total = item.get_total_price()
        total_amount += item_total
        print(f"{item.product.name} | Qty: {item.quantity} | "
              f"Price: Rs. {item.product.price:.2f} | Total: Rs. {item_total:.2f}")
    
    print("-" * 50)
    print(f"Total Amount: Rs. {total_amount:.2f}")
    print(f"Total Items: {cart.get_item_count()}")