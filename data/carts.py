"""
Cart and CartItem classes for shopping cart management
"""

from datetime import datetime
from typing import Dict, List
from data.exceptions import CartError


class CartItem:
    """Represents an item in the shopping cart"""
    
    def __init__(self, product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.__product = product
        self.__quantity = quantity
    
    @property
    def product(self):
        return self.__product
    
    @property
    def quantity(self) -> int:
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value: int):
        if value <= 0:
            raise ValueError("Quantity must be positive")
        self.__quantity = value
    
    def get_total_price(self) -> float:
        """Calculate total price for this cart item"""
        return self.__product.price * self.__quantity
    
    def __str__(self) -> str:
        return f"CartItem(product={self.__product.name}, quantity={self.__quantity})"


class Cart:
    """Represents a shopping cart"""
    
    def __init__(self, user_id: str):
        self.__user_id = user_id
        self.__items: Dict[str, CartItem] = {}
        self.__created_at = datetime.now()
    
    @property
    def user_id(self) -> str:
        return self.__user_id
    
    def add_item(self, product, quantity: int):
        """Add item to cart"""
        if not product.is_available(quantity):
            raise CartError(f"Product {product.name} is not available in required quantity")
        
        if product.product_id in self.__items:
            # Update existing item
            new_quantity = self.__items[product.product_id].quantity + quantity
            if not product.is_available(new_quantity):
                raise CartError(f"Cannot add {quantity} more items. Insufficient stock")
            self.__items[product.product_id].quantity = new_quantity
        else:
            # Add new item
            self.__items[product.product_id] = CartItem(product, quantity)
    
    def remove_item(self, product_id: str):
        """Remove item from cart"""
        if product_id not in self.__items:
            raise CartError(f"Product with ID {product_id} not found in cart")
        del self.__items[product_id]
    
    def update_quantity(self, product_id: str, quantity: int):
        """Update quantity of an item in cart"""
        if product_id not in self.__items:
            raise CartError(f"Product with ID {product_id} not found in cart")
        
        if quantity <= 0:
            self.remove_item(product_id)
        else:
            product = self.__items[product_id].product
            if not product.is_available(quantity):
                raise CartError(f"Cannot update quantity. Insufficient stock")
            self.__items[product_id].quantity = quantity
    
    def get_items(self) -> List[CartItem]:
        """Get all items in cart"""
        return list(self.__items.values())
    
    def get_total_amount(self) -> float:
        """Calculate total amount for all items in cart"""
        return sum(item.get_total_price() for item in self.__items.values())
    
    def get_item_count(self) -> int:
        """Get total number of items in cart"""
        return sum(item.quantity for item in self.__items.values())
    
    def is_empty(self) -> bool:
        """Check if cart is empty"""
        return len(self.__items) == 0
    
    def clear(self):
        """Clear all items from cart"""
        self.__items.clear()
    
    def __str__(self) -> str:
        return f"Cart(user_id={self.__user_id}, items={len(self.__items)})"


# Global carts storage
carts_data: Dict[str, Cart] = {}