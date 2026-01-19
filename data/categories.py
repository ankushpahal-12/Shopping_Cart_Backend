"""
Category class and category data management
"""

class Category:
    """Represents a product category"""
    
    def __init__(self, category_id: str, name: str, description: str = ""):
        self.__category_id = category_id
        self.__name = name
        self.__description = description
        self.__is_active = True
    
    @property
    def category_id(self) -> str:
        return self.__category_id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Category name cannot be empty")
        self.__name = value.strip()
    
    @property
    def description(self) -> str:
        return self.__description
    
    @description.setter
    def description(self, value: str):
        self.__description = value
    
    def is_active(self) -> bool:
        return self.__is_active
    
    def deactivate(self):
        """Deactivate the category"""
        self.__is_active = False
    
    def __str__(self) -> str:
        return f"Category(id={self.__category_id}, name={self.__name})"


# Demo categories data
categories_data = {
    "cat1": Category("cat1", "Electronics", "Electronic devices and gadgets"),
    "cat2": Category("cat2", "Clothing", "Fashion and apparel"),
    "cat3": Category("cat3", "Books", "Books and literature")
}