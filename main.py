"""
Main Shopping Application - OOP Design with Modular Structure
Entry point for the shopping application with user and admin interfaces
"""

# Import authentication functions
from Authentication.user_login import user_login, user_logout
from Authentication.admin_login import admin_login, admin_logout

# Import user functions
from user_Functions.view_catalog import view_catalog
from user_Functions.add_to_cart import add_to_cart
from user_Functions.remove_from_cart import remove_from_cart
from user_Functions.view_cart import view_cart
from user_Functions.checkout import checkout

# Import admin functions
from AdminFunctions.add_product import add_product
from AdminFunctions.update_product import update_product
from AdminFunctions.delete_product import delete_product
from AdminFunctions.add_category import add_category
from AdminFunctions.delete_category import delete_category

# Import data for admin views
from data.products import products_data
from data.categories import categories_data
from data.exceptions import AuthenticationError, CartError, PaymentError, ProductNotFoundError, CategoryNotFoundError


def admin_view_products(session_id: str):
    """View all products (admin function)"""
    from Authentication.admin_login import validate_admin_session
    validate_admin_session(session_id)
    
    print("\n=== All Products (Admin View) ===")
    if not products_data:
        print("No products found.")
        return
    
    for product in products_data.values():
        category = categories_data.get(product.category_id)
        category_name = category.name if category else "Unknown"
        status = "Active" if product.is_active() else "Inactive"
        
        print(f"ID: {product.product_id} | {product.name} | Rs. {product.price:.2f}")
        print(f"Category: {category_name} | Stock: {product.stock} | Status: {status}")
        print(f"Description: {product.description}")
        print("-" * 50)


def admin_view_categories(session_id: str):
    """View all categories (admin function)"""
    from Authentication.admin_login import validate_admin_session
    validate_admin_session(session_id)
    
    print("\n=== All Categories (Admin View) ===")
    if not categories_data:
        print("No categories found.")
        return
    
    for category in categories_data.values():
        status = "Active" if category.is_active() else "Inactive"
        product_count = len([p for p in products_data.values() 
                           if p.category_id == category.category_id and p.is_active()])
        
        print(f"ID: {category.category_id} | {category.name} | Status: {status}")
        print(f"Products: {product_count} | Description: {category.description}")
        print("-" * 50)


def admin_menu(session_id: str):
    """Display and handle admin menu"""
    while True:
        print("\n=== Admin Panel ===")
        print("1. Add Product")
        print("2. Update Product") 
        print("3. Delete Product")
        print("4. Add Category")
        print("5. Delete Category")
        print("6. View All Products")
        print("7. View All Categories")
        print("8. Logout")
        
        try:
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == "1":
                # Add Product
                name = input("Enter product name: ").strip()
                price = float(input("Enter product price: "))
                
                # Show available categories
                admin_view_categories(session_id)
                category_id = input("Enter category ID: ").strip()
                description = input("Enter product description (optional): ").strip()
                stock = int(input("Enter initial stock: "))
                
                add_product(session_id, name, price, category_id, description, stock)
            
            elif choice == "2":
                # Update Product
                admin_view_products(session_id)
                product_id = input("Enter product ID to update: ").strip()
                
                print("Leave blank to keep current value:")
                name = input("Enter new name: ").strip() or None
                price_str = input("Enter new price: ").strip()
                price = float(price_str) if price_str else None
                description = input("Enter new description: ").strip() or None
                stock_str = input("Enter new stock: ").strip()
                stock = int(stock_str) if stock_str else None
                
                update_product(session_id, product_id, name, price, description, stock)
            
            elif choice == "3":
                # Delete Product
                admin_view_products(session_id)
                product_id = input("Enter product ID to delete: ").strip()
                delete_product(session_id, product_id)
            
            elif choice == "4":
                # Add Category
                name = input("Enter category name: ").strip()
                description = input("Enter category description (optional): ").strip()
                add_category(session_id, name, description)
            
            elif choice == "5":
                # Delete Category
                admin_view_categories(session_id)
                category_id = input("Enter category ID to delete: ").strip()
                delete_category(session_id, category_id)
            
            elif choice == "6":
                # View All Products
                admin_view_products(session_id)
            
            elif choice == "7":
                # View All Categories
                admin_view_categories(session_id)
            
            elif choice == "8":
                # Logout
                admin_logout(session_id)
                break
            
            else:
                print("Invalid choice. Please try again.")
                
        except (ValueError, ProductNotFoundError, CategoryNotFoundError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def user_menu(session_id: str):
    """Display and handle user menu"""
    while True:
        print("\n=== User Panel ===")
        print("1. View Catalog")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove from Cart")
        print("5. Checkout")
        print("6. Logout")
        
        try:
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == "1":
                # View Catalog
                view_catalog(session_id)
            
            elif choice == "2":
                # Add to Cart
                view_catalog(session_id)
                product_id = input("Enter product ID to add to cart: ").strip()
                quantity = int(input("Enter quantity: "))
                add_to_cart(session_id, product_id, quantity)
            
            elif choice == "3":
                # View Cart
                view_cart(session_id)
            
            elif choice == "4":
                # Remove from Cart
                view_cart(session_id)
                product_id = input("Enter product ID to remove from cart: ").strip()
                remove_from_cart(session_id, product_id)
            
            elif choice == "5":
                # Checkout
                view_cart(session_id)
                print("\nPayment Methods:")
                print("1. UPI")
                print("2. DEBIT_CARD")
                print("3. NET_BANKING")
                
                payment_choice = input("Select payment method (1-3): ").strip()
                payment_methods = {"1": "UPI", "2": "DEBIT_CARD", "3": "NET_BANKING"}
                
                if payment_choice in payment_methods:
                    payment_method = payment_methods[payment_choice]
                    checkout(session_id, payment_method)
                else:
                    print("Invalid payment method selected.")
            
            elif choice == "6":
                # Logout
                user_logout(session_id)
                break
            
            else:
                print("Invalid choice. Please try again.")
                
        except (ValueError, CartError, PaymentError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def main():
    """Main function to run the shopping application"""
    print("Welcome to the Demo Marketplace")
    print("=" * 40)
    
    while True:
        try:
            print("\n1. User Login")
            print("2. Admin Login")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == "1":
                # User Login
                username = input("Enter username: ").strip()
                password = input("Enter password: ").strip()
                try:
                    session_id = user_login(username, password)
                    user_menu(session_id)
                except AuthenticationError:
                    continue
            
            elif choice == "2":
                # Admin Login
                username = input("Enter admin username: ").strip()
                password = input("Enter admin password: ").strip()
                try:
                    session_id = admin_login(username, password)
                    admin_menu(session_id)
                except AuthenticationError:
                    continue
            
            elif choice == "3":
                # Exit
                print("Thank you for using Demo Marketplace!")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("\n\nExiting application...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()