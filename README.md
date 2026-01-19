# Shopping_Cart_Backend
The Shopping Application using Python is a backend-based console project developed to simulate the fundamental operations of an e-commerce system using Object-Oriented Programming (OOP) principles. The application emphasizes backend business logic without incorporating any graphical user interface or database connectivity.
A complete backend shopping system built with proper OOP design principles and modular structure. This application demonstrates industry-standard Python development practices with comprehensive error handling, role-based access control, and modular architecture.

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Installation & Setup

1. **Download/Clone the Project**
   ```bash
   # If using git
   git clone https://github.com/ankushpahal-12/Shopping_Cart_Backend
   
   # Or download and extract the ZIP file
   ```

2. **Navigate to Project Directory**
   ```bash
   cd Shopping_Cart_Backend
   ```

3. **Run the Application**
   ```bash
   python main.py
   ```

4. **Test the Application (Optional)**
   ```bash
   # Run from parent directory
   cd ..
   python test_modular_app.py
   ```

### 🔐 Login Credentials

**Users:**
- Username: `john_doe` | Password: `password123`
- Username: `jane_smith` | Password: `password456`

**Admin:**
- Username: `admin` | Password: `admin123`

## ✨ Features

- **User Authentication**: Secure login system for users and admins
- **Session Management**: UUID-based session handling
- **Product Management**: Full CRUD operations for products and categories
- **Shopping Cart**: Add, remove, and manage cart items
- **Payment Processing**: Support for UPI, Debit Card, and Net Banking
- **Role-based Access Control**: Strict separation between user and admin functions
- **Exception Handling**: Comprehensive error handling with custom exceptions

## 📁 Project Structure

```
simplilearn_project/
├── main.py                        # 🎯 Main application entry point
├── README.md                      # 📖 This documentation file
├── __init__.py                    # 📦 Package initialization
├── data/                          # 💾 Data models and storage
│   ├── __init__.py
│   ├── exceptions.py              # ⚠️ Custom exception classes
│   ├── users.py                   # 👤 User class and demo data
│   ├── admin.py                   # 🔧 Admin class and demo data
│   ├── products.py                # 📦 Product class and demo data
│   ├── categories.py              # 📂 Category class and demo data
│   ├── carts.py                   # 🛒 Cart and CartItem classes
│   ├── sessions.py                # 🔐 Authentication and session management
│   └── payment.py                 # 💳 Payment processing system
├── Authentication/                # 🔑 Authentication modules
│   ├── __init__.py
│   ├── user_login.py              # 👤 User login/logout functions
│   └── admin_login.py             # 🔧 Admin login/logout functions
├── user_Functions/                # 👥 User-specific functions
│   ├── __init__.py
│   ├── view_catalog.py            # 📋 View product catalog
│   ├── add_to_cart.py             # ➕ Add products to cart
│   ├── remove_from_cart.py        # ➖ Remove products from cart
│   ├── view_cart.py               # 👀 View cart contents
│   └── checkout.py                # 💰 Checkout and payment processing
└── AdminFunctions/                # 🛠️ Admin-specific functions
    ├── __init__.py
    ├── add_product.py             # ➕ Add new products
    ├── update_product.py          # ✏️ Update existing products
    ├── delete_product.py          # 🗑️ Delete products
    ├── add_category.py            # ➕ Add new categories
    └── delete_category.py         # 🗑️ Delete categories
```

## 🏗️ Implementation Details

### OOP Architecture

This application follows a **layered architecture** with clear separation of concerns:

1. **Data Layer** (`data/`): Contains all data models, storage, and business logic
2. **Authentication Layer** (`Authentication/`): Handles user and admin authentication
3. **Service Layer** (`user_Functions/`, `AdminFunctions/`): Contains business operations
4. **Presentation Layer** (`main.py`): Terminal-based user interface

### Core Classes Implementation

#### 1. **User Class** (`data/users.py`)
```python
class User:
    - Private attributes: __user_id, __username, __password, __email
    - Properties: user_id, username, email (read-only)
    - Methods: verify_password(), is_active()
    - Encapsulation: Password is private and verified through method
```

#### 2. **Admin Class** (`data/admin.py`)
```python
class Admin:
    - Similar structure to User but with admin privileges
    - Separate authentication and session management
    - Role-based access control implementation
```

#### 3. **Product Class** (`data/products.py`)
```python
class Product:
    - Attributes: product_id, name, price, category_id, description, stock
    - Property setters with validation (price >= 0, stock >= 0)
    - Methods: is_available(), reduce_stock(), increase_stock(), deactivate()
    - Business logic for stock management
```

#### 4. **Category Class** (`data/categories.py`)
```python
class Category:
    - Attributes: category_id, name, description
    - Property setters with validation
    - Methods: deactivate()
    - Relationship management with products
```

#### 5. **Cart & CartItem Classes** (`data/carts.py`)
```python
class CartItem:
    - Represents individual items in cart
    - Quantity validation and total price calculation

class Cart:
    - User-specific shopping cart
    - Methods: add_item(), remove_item(), get_total_amount()
    - Stock validation before adding items
```

#### 6. **Authentication Class** (`data/sessions.py`)
```python
class Authentication:
    - UUID-based session management
    - Separate user and admin sessions
    - Methods: login_user(), login_admin(), validate_session()
    - Session cleanup on logout
```

#### 7. **Payment Class** (`data/payment.py`)
```python
class Payment:
    - Multiple payment methods support
    - Transaction ID generation
    - Payment validation and processing
    - Transaction history storage
```

### Exception Handling System

#### Custom Exception Classes (`data/exceptions.py`)
- `AuthenticationError`: Login failures, invalid credentials
- `AuthorizationError`: Permission denied, invalid sessions
- `ProductNotFoundError`: Product lookup failures
- `CategoryNotFoundError`: Category lookup failures
- `CartError`: Cart operations (empty cart, invalid quantities)
- `PaymentError`: Payment processing failures

#### Exception Handling Strategy
```python
try:
    # Business operation
    result = perform_operation()
except SpecificError as e:
    print(f"User-friendly error message: {e}")
    raise  # Re-raise for higher-level handling
```

### Session Management Implementation

#### UUID-Based Sessions
```python
import uuid

# Session creation
session_id = str(uuid.uuid4())
self.__user_sessions[session_id] = user_id

# Session validation
def validate_session(session_id):
    return self.__sessions.get(session_id)
```

#### Role-Based Access Control
```python
def validate_admin_session(session_id):
    admin_id = auth_manager.validate_admin_session(session_id)
    if not admin_id:
        raise AuthorizationError("Admin access required")
    return admin_id
```

## 📊 Demo Data

### 👤 Users (in `data/users.py`)
| Username | Password | Email | User ID |
|----------|----------|-------|---------|
| john_doe | password123 | john@email.com | user1 |
| jane_smith | password456 | jane@email.com | user2 |

### 🔧 Admin (in `data/admin.py`)
| Username | Password | Email | Admin ID |
|----------|----------|-------|----------|
| admin | admin123 | admin@email.com | admin1 |

### 📂 Categories (in `data/categories.py`)
| Category ID | Name | Description |
|-------------|------|-------------|
| cat1 | Electronics | Electronic devices and gadgets |
| cat2 | Clothing | Fashion and apparel |
| cat3 | Books | Books and literature |

### 📦 Products (in `data/products.py`)
| Product ID | Name | Price (Rs.) | Category | Stock | Description |
|------------|------|-------------|----------|-------|-------------|
| prod1 | Smartphone | 25,000 | Electronics | 10 | Latest smartphone |
| prod2 | Laptop | 55,000 | Electronics | 5 | Gaming laptop |
| prod3 | T-Shirt | 500 | Clothing | 20 | Cotton t-shirt |
| prod4 | Jeans | 1,500 | Clothing | 15 | Denim jeans |
| prod5 | Python Book | 800 | Books | 8 | Learn Python programming |

## 🎮 Usage Guide

### Step-by-Step Application Flow

#### 1. **Starting the Application**
```bash
cd Shopping_Cart_Backend
python main.py
```

**Expected Output:**
```
Welcome to the Demo Marketplace
========================================

1. User Login
2. Admin Login
3. Exit
Enter your choice (1-3):
```

#### 2. **User Login Flow**
```
Choice: 1
Enter username: john_doe
Enter password: password123
```

**Expected Output:**
```
Welcome john_doe! Login successful.

=== User Panel ===
1. View Catalog
2. Add to Cart
3. View Cart
4. Remove from Cart
5. Checkout
6. Logout
```

#### 3. **User Operations**

##### **View Catalog (Option 1)**
```
=== Product Catalog ===
ID: prod1 | Smartphone | Rs. 25000.00
Category: Electronics | Stock: 10
Description: Latest smartphone
--------------------------------------------------
ID: prod2 | Laptop | Rs. 55000.00
Category: Electronics | Stock: 5
Description: Gaming laptop
--------------------------------------------------
[... more products ...]
```

##### **Add to Cart (Option 2)**
```
Enter product ID to add to cart: prod1
Enter quantity: 2
Added 2 x Smartphone to cart successfully!
```

##### **View Cart (Option 3)**
```
=== Your Cart ===
Smartphone | Qty: 2 | Price: Rs. 25000.00 | Total: Rs. 50000.00
--------------------------------------------------
Total Amount: Rs. 50000.00
Total Items: 2
```

##### **Checkout (Option 5)**
```
=== Your Cart ===
[Cart contents displayed]

Payment Methods:
1. UPI
2. DEBIT_CARD
3. NET_BANKING
Select payment method (1-3): 1

Your order is successfully placed
You will be redirected to UPI to make a payment of Rs. 50000.00
Transaction ID: a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

#### 4. **Admin Login Flow**
```
Choice: 2
Enter admin username: admin
Enter admin password: admin123
```

**Expected Output:**
```
Welcome Admin admin! Login successful.

=== Admin Panel ===
1. Add Product
2. Update Product
3. Delete Product
4. Add Category
5. Delete Category
6. View All Products
7. View All Categories
8. Logout
```

#### 5. **Admin Operations**

##### **Add Product (Option 1)**
```
Enter product name: Tablet
Enter product price: 15000
[Categories displayed]
Enter category ID: cat1
Enter product description (optional): Android tablet
Enter initial stock: 12
Product 'Tablet' added successfully with ID: prod6
```

##### **Update Product (Option 2)**
```
[All products displayed]
Enter product ID to update: prod1
Leave blank to keep current value:
Enter new name: [Enter or leave blank]
Enter new price: 26000
Enter new description: [Enter or leave blank]
Enter new stock: 15
Product 'Smartphone' updated successfully!
```

##### **Delete Product (Option 3)**
```
[All products displayed]
Enter product ID to delete: prod6
Product 'Tablet' deleted successfully!
```

### 🔄 Complete User Journey Example

1. **Login as User**
   - Username: `john_doe`, Password: `password123`

2. **Browse Products**
   - Select option 1 (View Catalog)
   - See all available products with prices and stock

3. **Add Items to Cart**
   - Select option 2 (Add to Cart)
   - Add prod1 (Smartphone) quantity 1
   - Add prod3 (T-Shirt) quantity 2

4. **Review Cart**
   - Select option 3 (View Cart)
   - See total: Rs. 26,000 (25,000 + 1,000)

5. **Checkout**
   - Select option 5 (Checkout)
   - Choose payment method (UPI)
   - Get confirmation and transaction ID

6. **Logout**
   - Select option 6 (Logout)

## 🔧 Technical Implementation

### Dependencies
- **Python 3.7+** (No external libraries required)
- **Standard Library Modules Used:**
  - `uuid` - For session ID generation
  - `datetime` - For timestamps
  - `typing` - For type hints

### Key Features Implementation

#### **OOP Principles Applied**
- **Encapsulation**: Private attributes with property decorators
- **Modularity**: Separate files for different functionalities
- **Abstraction**: Clear interfaces between components
- **Data Hiding**: Protected internal state of objects

#### **Security Features**
- Session-based authentication with UUID
- Role-based access control (RBAC)
- Input validation and sanitization
- Password verification (demo implementation)
- Authorization checks for all operations

#### **Error Handling Strategy**
- Custom exception classes for different error types
- Try-catch blocks in all user interactions
- Graceful error messages for users
- Application never crashes on invalid input
- Proper error propagation through layers

#### **Payment System Architecture**
- Multiple payment methods (UPI, Debit Card, Net Banking)
- Transaction ID generation using UUID
- Payment confirmation messages
- Stock reduction after successful payment
- Transaction history storage

#### **Data Management**
- In-memory data structures (dictionaries and lists)
- Object-oriented data models
- Relationship management between entities
- Data validation at model level

### File Dependencies Map

```
main.py
├── Authentication/
│   ├── user_login.py → data/users.py, data/sessions.py
│   └── admin_login.py → data/admin.py, data/sessions.py
├── user_Functions/
│   ├── view_catalog.py → data/products.py, data/categories.py
│   ├── add_to_cart.py → data/products.py, data/carts.py
│   ├── remove_from_cart.py → data/carts.py
│   ├── view_cart.py → data/carts.py
│   └── checkout.py → data/carts.py, data/payment.py
├── AdminFunctions/
│   ├── add_product.py → data/products.py, data/categories.py
│   ├── update_product.py → data/products.py
│   ├── delete_product.py → data/products.py
│   ├── add_category.py → data/categories.py
│   └── delete_category.py → data/categories.py, data/products.py
└── data/
    ├── exceptions.py (Base exception classes)
    ├── users.py (User class + demo data)
    ├── admin.py (Admin class + demo data)
    ├── products.py (Product class + demo data)
    ├── categories.py (Category class + demo data)
    ├── carts.py (Cart/CartItem classes)
    ├── sessions.py (Authentication class)
    └── payment.py (Payment class)
```

## 🧪 Testing & Validation

### Running Tests

#### **Automated Test Suite**
```bash
# Run from parent directory of simplilearn_project
python test_modular_app.py
```

**Expected Test Output:**
```
✓ All imports successful!
✓ User login successful. Session: 0c31bb1c...
✓ Found 5 products
✓ Product added to cart
✓ Admin login successful. Session: cbe7be03...
✓ Product added with ID: prod6
✓ Authorization working correctly: AuthorizationError
✓ Both user and admin logged out successfully
=== All Tests Completed Successfully! ===
```

#### **Manual Testing Checklist**

**User Functions:**
- [ ] User login with valid credentials
- [ ] User login with invalid credentials (should fail)
- [ ] View product catalog
- [ ] Add products to cart
- [ ] View cart contents
- [ ] Remove products from cart
- [ ] Checkout with different payment methods
- [ ] User logout

**Admin Functions:**
- [ ] Admin login with valid credentials
- [ ] Admin login with invalid credentials (should fail)
- [ ] Add new product
- [ ] Update existing product
- [ ] Delete product
- [ ] Add new category
- [ ] Delete category (with/without products)
- [ ] View all products and categories
- [ ] Admin logout

**Security Tests:**
- [ ] User cannot access admin functions
- [ ] Invalid session handling
- [ ] Session expiration after logout

**Error Handling Tests:**
- [ ] Invalid product ID in cart operations
- [ ] Insufficient stock scenarios
- [ ] Empty cart checkout
- [ ] Invalid payment methods

### Performance Considerations

- **Memory Usage**: All data stored in-memory (suitable for demo)
- **Session Management**: Efficient UUID-based sessions
- **Data Access**: O(1) dictionary lookups for most operations
- **Scalability**: Modular design allows easy extension

### Code Quality Metrics

- **Lines of Code**: ~1,200 lines across all modules
- **Classes**: 8 core classes with proper encapsulation
- **Functions**: 25+ functions with clear responsibilities
- **Exception Classes**: 6 custom exception types
- **Documentation**: Comprehensive docstrings and comments

## 📋 Expected Output Messages

### Successful Operations
- `"Welcome to the Demo Marketplace"`
- `"Welcome [username]! Login successful."`
- `"Welcome Admin [username]! Login successful."`
- `"Your order is successfully placed"`
- `"You will be redirected to UPI to make a payment of Rs. XXXX"`
- `"Product '[name]' added successfully with ID: [id]"`
- `"Product '[name]' updated successfully!"`
- `"Category '[name]' added successfully with ID: [id]"`

### Error Messages
- `"Login failed: Invalid username or password"`
- `"Error adding to cart: Product [name] is not available in required quantity"`
- `"Checkout failed: Cannot checkout with empty cart"`
- `"Error: Product with ID [id] not found"`
- `"Authorization working correctly: AuthorizationError"`

## 🎯 Academic Requirements Fulfilled

### ✅ **Project Requirements Met**

| Requirement | Implementation | Location |
|-------------|----------------|----------|
| Backend-only Python application | ✅ Terminal-based interface, no GUI | `main.py` |
| In-memory data structures only | ✅ Dictionaries and lists for storage | `data/*.py` |
| Proper OOP principles | ✅ 8 classes with encapsulation | All modules |
| Robust exception handling | ✅ 6 custom exception classes | `data/exceptions.py` |
| User/Admin authentication | ✅ UUID sessions, role-based access | `Authentication/` |
| Product & Category management | ✅ Full CRUD operations | `AdminFunctions/` |
| Cart management | ✅ Add/remove/view/checkout | `user_Functions/` |
| Payment simulation | ✅ 3 payment methods | `data/payment.py` |
| Modular code structure | ✅ Separate files per functionality | Entire project |

### ✅ **OOP Principles Demonstrated**

1. **Encapsulation**: Private attributes (`__attribute`) with property decorators
2. **Abstraction**: Clear class interfaces and method signatures
3. **Modularity**: Separate concerns across different modules
4. **Data Hiding**: Internal state protection and controlled access
5. **Composition**: Cart contains CartItems, relationships between classes
6. **Polymorphism**: Common interfaces for User and Admin classes

### ✅ **Industry Standards Applied**

- **Clean Code**: Meaningful names, single responsibility principle
- **Documentation**: Comprehensive docstrings and comments
- **Error Handling**: Graceful failure handling, user-friendly messages
- **Security**: Session management, input validation, authorization
- **Testing**: Automated test suite with comprehensive coverage
- **Maintainability**: Modular structure, easy to extend and modify

## 🚀 Future Enhancements

### Possible Extensions
- Database integration (SQLite/PostgreSQL)
- REST API implementation with Flask/FastAPI
- Web frontend with HTML/CSS/JavaScript
- Advanced authentication (JWT tokens, password hashing)
- Email notifications for orders
- Inventory management system
- Order history and tracking
- Multi-currency support
- Advanced search and filtering

### Scalability Considerations
- Database abstraction layer
- Caching mechanisms
- Load balancing for multiple users
- Microservices architecture
- API rate limiting
- Logging and monitoring

---

## 📞 Support & Documentation

For questions about implementation details or academic evaluation:

1. **Code Structure**: Review the modular file organization
2. **OOP Concepts**: Examine class definitions and relationships
3. **Error Handling**: Test various failure scenarios
4. **Business Logic**: Follow the user/admin workflows
5. **Testing**: Run the automated test suite

This implementation serves as a comprehensive example of Object-Oriented Programming principles in Python, suitable for academic evaluation, viva presentations, and real-world application development learning.
