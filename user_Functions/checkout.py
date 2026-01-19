"""
Checkout and payment processing functionality for users
"""

from Authentication.user_login import validate_user_session
from data.carts import carts_data
from data.payment import payment_processor
from data.exceptions import CartError, PaymentError


def checkout(session_id: str, payment_method: str):
    """
    Checkout and process payment (user function)
    
    Args:
        session_id: User's session identifier
        payment_method: Payment method (UPI, DEBIT_CARD, NET_BANKING)
    
    Returns:
        transaction_id: Transaction identifier if successful
    
    Raises:
        AuthenticationError: If session is invalid
        CartError: If cart is empty or has issues
        PaymentError: If payment processing fails
    """
    # Validate user session
    user_id = validate_user_session(session_id)
    
    try:
        # Check if user has items in cart
        if user_id not in carts_data or carts_data[user_id].is_empty():
            raise CartError("Cannot checkout with empty cart")
        
        cart = carts_data[user_id]
        total_amount = cart.get_total_amount()
        
        # Validate stock availability for all items
        for item in cart.get_items():
            if not item.product.is_available(item.quantity):
                raise CartError(f"Product {item.product.name} is not available in required quantity")
        
        # Process payment
        transaction_id = payment_processor.process_payment(total_amount, payment_method, user_id)
        
        # Reduce stock for all items
        for item in cart.get_items():
            item.product.reduce_stock(item.quantity)
        
        # Clear cart after successful payment
        cart.clear()
        
        # Display success messages
        print("Your order is successfully placed")
        print(payment_processor.get_payment_message(payment_method, total_amount))
        print(f"Transaction ID: {transaction_id}")
        
        return transaction_id
        
    except (CartError, PaymentError) as e:
        print(f"Checkout failed: {e}")
        raise
