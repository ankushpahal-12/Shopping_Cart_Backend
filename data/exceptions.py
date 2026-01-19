"""
Custom Exception Classes for the Shopping Application
"""

class AuthenticationError(Exception):
    """Raised when authentication fails"""
    pass


class AuthorizationError(Exception):
    """Raised when user lacks permission for an operation"""
    pass


class ProductNotFoundError(Exception):
    """Raised when a product is not found"""
    pass


class CategoryNotFoundError(Exception):
    """Raised when a category is not found"""
    pass


class CartError(Exception):
    """Raised for cart-related errors"""
    pass


class PaymentError(Exception):
    """Raised for payment-related errors"""
    pass