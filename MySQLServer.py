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


import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server (change user and password as needed)
    conn = mysql.connector.connect(
        host='localhost',
        user='your_username',      # Replace with your MySQL username
        password='your_password'   # Replace with your MySQL password
    )

    cursor = conn.cursor()

    # Try to create database
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

except mysql.connector.Error as err:
    print(f"Error: Could not connect to MySQL server.\n{err}")

finally:
    # Cleanup: close cursor and connection if they were opened
    try:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    except NameError:
        pass
        

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
# File: MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None

    try:
        # Connect to MySQL Server (update with your credentials)
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error: {err}")

    except Exception as ex:
        print(f"Unexpected error: {ex}")

    finally:
        if cursor:
            try:
                cursor.close()
            except Error as cursor_err:
                print(f"Error closing cursor: {cursor_err}")

        if connection and connection.is_connected():
            try:
                connection.close()
                print("MySQL connection closed.")
            except Error as conn_err:
                print(f"Error closing connection: {conn_err}")

if __name__ == "__main__":
    create_database()
