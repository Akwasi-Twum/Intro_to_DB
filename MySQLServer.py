# File: MySQLServer.py
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",      # Replace with your host
            user="your_username",  # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        # Handle any connection or execution errors
        print(f"




# File: MySQLServer.py

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (adjust credentials as needed)
    connection = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password'
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Use CREATE DATABASE IF NOT EXISTS to avoid failure if the DB already exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Ensure resources are released properly
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
