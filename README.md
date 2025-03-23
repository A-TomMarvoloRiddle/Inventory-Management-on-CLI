# Kaljio Inventory Management System 🛒

Welcome to the Kaljio E-commerce platform! This is a simple project demonstrating a product catalog and login functionality using MySQL and Python.

## Features ✨
- **Product Management**: Displays a catalog of products, each with details like name, price, and features.
- **User Authentication**: Basic login system to authenticate admin users.
- **Database-Driven**: Data is stored in a MySQL database for managing products and user credentials.

## File Structure 📁
- **`Project_Tables.txt`**: Contains the SQL queries to create the `kaljio` database, tables for products and login, and insert sample data.
- **`KalJio Gadgetronics.py`**: Python code that interacts with the database & gives command line interface.

## Database Setup ⚙️
Before running the Python code, make sure you set up the MySQL database by running the following SQL queries. You can do this in your MySQL client:

### SQL Queries 📝
1. **Create the Database**: First, create the `kaljio` database. 
2. **Create `product` Table**: Create a table to store product information.
3. **Create `login` Table**: Create a table for storing login credentials for admin users.
4. **Insert Sample Data**: Insert sample products and users to get started.

### Database Tables 📊
- **`product` Table**: Stores product details like product number, name, company, features, and price.
- **`login` Table**: Stores login credentials for admin users.

Once the database is set up, you can run the Python code to interact with it.

## Running the Python Code 🏃‍♂️
- After setting up the database, run the Python code (`KalJio Gadgetronics.py`).
- The code will connect to the database and allow you to view, add, update, or delete products.
- Admin login credentials are provided in the code to authenticate and access the product management system.


## Dependencies 📦
To run this project, you need to install the following Python dependencies:

- **mysql.connector**: To connect Python to MySQL and interact with the database.
- **prettytable**: To format and display product data in a tabular format.

You can install these dependencies using pip. 
Run the following command in your terminal:
```
pip install mysql.connector prettytable
```
---

This project is a simple demonstration of how to manage an e-commerce catalog with Python and MySQL.
