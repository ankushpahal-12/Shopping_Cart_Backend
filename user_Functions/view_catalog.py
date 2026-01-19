"""
View product catalog functionality for users
"""

from typing import List
from Authentication.user_login import validate_user_session
from data.products import products_data
from data.categories import categories_data


def view_catalog(session_id: str) -> List:
    """
    View product catalog (user function)
    
    Args:
        session_id: User's session identifier
    
    Returns:
        List of active products
    
    Raises:
        AuthenticationError: If session is invalid
    """
    # Validate user session
    validate_user_session(session_id)
    
    # Get active products
    active_products = [p for p in products_data.values() if p.is_active()]
    
    print("\n=== Product Catalog ===")
    if not active_products:
        print("No products available.")
        return []
    
    for product in active_products:
        category = categories_data.get(product.category_id)
        category_name = category.name if category else "Unknown"
        print(f"ID: {product.product_id} | {product.name} | Rs. {product.price:.2f}")
        print(f"Category: {category_name} | Stock: {product.stock}")
        print(f"Description: {product.description}")
        print("-" * 50)
    
    return active_products