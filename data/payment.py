"""
Payment processing functionality
"""

import uuid
from datetime import datetime
from typing import Dict, Optional
from data.exceptions import PaymentError


class Payment:
    """Handles payment processing"""
    
    PAYMENT_METHODS = ["UPI", "DEBIT_CARD", "NET_BANKING"]
    
    def __init__(self):
        self.__transactions: Dict[str, Dict] = {}
    
    def process_payment(self, amount: float, payment_method: str, 
                       user_id: str) -> str:
        """Process payment and return transaction ID"""
        if payment_method not in self.PAYMENT_METHODS:
            raise PaymentError(f"Invalid payment method. Supported methods: {', '.join(self.PAYMENT_METHODS)}")
        
        if amount <= 0:
            raise PaymentError("Payment amount must be positive")
        
        # Generate transaction ID
        transaction_id = str(uuid.uuid4())
        
        # Store transaction details
        self.__transactions[transaction_id] = {
            "amount": amount,
            "payment_method": payment_method,
            "user_id": user_id,
            "timestamp": datetime.now(),
            "status": "SUCCESS"
        }
        
        return transaction_id
    
    def get_transaction(self, transaction_id: str) -> Optional[Dict]:
        """Get transaction details"""
        return self.__transactions.get(transaction_id)
    
    def get_payment_message(self, payment_method: str, amount: float) -> str:
        """Get appropriate payment message"""
        messages = {
            "UPI": f"You will be redirected to UPI to make a payment of Rs. {amount:.2f}",
            "DEBIT_CARD": f"You will be redirected to your bank to make a payment of Rs. {amount:.2f}",
            "NET_BANKING": f"You will be redirected to Net Banking to make a payment of Rs. {amount:.2f}"
        }
        return messages.get(payment_method, f"Payment of Rs. {amount:.2f} will be processed")


# Global payment processor
payment_processor = Payment()