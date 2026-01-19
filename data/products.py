"""
Product class and product data management
"""

class Product:
    """Represents a product in the shopping system"""
    
    def __init__(self, product_id: str, name: str, price: float, 
                 category_id: str, description: str = "", stock: int = 0):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__category_id = category_id
        self.__description = description
        self.__stock = stock
        self.__is_active = True
    
    @property
    def product_id(self) -> str:
        return self.__product_id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Product name cannot be empty")
        self.__name = value.strip()
    
    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value
    
    @property
    def category_id(self) -> str:
        return self.__category_id
    
    @property
    def description(self) -> str:
        return self.__description
    
    @description.setter
    def description(self, value: str):
        self.__description = value
    
    @property
    def stock(self) -> int:
        return self.__stock
    
    @stock.setter
    def stock(self, value: int):
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self.__stock = value
    
    def is_active(self) -> bool:
        return self.__is_active
    
    def is_available(self, quantity: int = 1) -> bool:
        """Check if product is available in required quantity"""
        return self.__is_active and self.__stock >= quantity
    
    def reduce_stock(self, quantity: int):
        """Reduce stock by given quantity"""
        if quantity > self.__stock:
            raise ValueError("Insufficient stock")
        self.__stock -= quantity
    
    def increase_stock(self, quantity: int):
        """Increase stock by given quantity"""
        self.__stock += quantity
    
    def deactivate(self):
        """Deactivate the product"""
        self.__is_active = False
    
    def __str__(self) -> str:
        return f"Product(id={self.__product_id}, name={self.__name}, price={self.__price})"


# Demo products data
products_data = {
    "prod1": Product("prod1", "Smartphone", 25000.0, "cat1", "Latest smartphone", 10),
    "prod2": Product("prod2", "Laptop", 55000.0, "cat1", "Gaming laptop", 5),
    "prod3": Product("prod3", "T-Shirt", 500.0, "cat2", "Cotton t-shirt", 20),
    "prod4": Product("prod4", "Jeans", 1500.0, "cat2", "Denim jeans", 15),
    "prod5": Product("prod5", "Python Book", 800.0, "cat3", "Learn Python programming", 8)
}