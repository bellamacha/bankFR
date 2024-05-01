from database import Database
from decimal import Decimal
import mysql.connector
import unittest


class UserFunctions:
    def __init__(self):
        self.db = Database()
    
    def create_user(self, account_number, pin, first_name, last_name, balance, email, phone_number, dob):
        query = """
            INSERT INTO users (account_number, pin, first_name, last_name, balance, email, phone_number, dob)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (account_number, pin, first_name, last_name, balance, email, phone_number, dob)
        self.db.cursor.execute(query, values)
        self.db.conn.commit()
    
    def delete_user(self, account_number):
        query = "DELETE FROM users WHERE account_number = %s"
        self.db.cursor.execute(query, (account_number,))
        self.db.conn.commit()
    
    def authenticate(self, email, pin):
        query = "SELECT * FROM users WHERE email = %s AND pin = %s"
        self.db.cursor.execute(query, (email, pin))
        user = self.db.cursor.fetchone()
        if user:
            return True
        else:
            return False

    def get_user_info(self, email):
        query = "SELECT * FROM users WHERE email = %s"
        self.db.cursor.execute(query, (email,))
        user_info = self.db.cursor.fetchone()
        if user_info:
            return {
                "first_name": user_info[3],
                "last_name": user_info[4],
                "pin": user_info[2],
                "email": user_info[5],
                "phone_number": user_info[6]
            }
        else:
            return None

    def update_user_info(self, account_number, first_name, last_name, pin, email, phone_number):
        query = """
            UPDATE users 
            SET first_name = %s, last_name = %s, pin = %s, email = %s, phone_number = %s 
            WHERE account_number = %s
        """
        values = (first_name, last_name, pin, email, phone_number, account_number)
        self.db.cursor.execute(query, values)
        self.db.conn.commit()

    def check_balance(self, account_number):
        query = "SELECT balance FROM users WHERE account_number = %s"
        self.db.cursor.execute(query, (account_number,))
        result = self.db.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    
    def deposit(self, account_number, amount):
        current_balance = self.check_balance(account_number)
        if current_balance is not None:
            new_balance = current_balance + Decimal(str(amount))
            query = "UPDATE users SET balance = %s WHERE account_number = %s"
            self.db.cursor.execute(query, (new_balance, account_number))
            self.db.conn.commit()
            return True
        else:
            return False
    
    def withdraw(self, account_number, amount):
        current_balance = self.check_balance(account_number)
        if current_balance is not None:
            if current_balance >= amount:
                new_balance = current_balance - Decimal(str(amount))
                query = "UPDATE users SET balance = %s WHERE account_number = %s"
                self.db.cursor.execute(query, (new_balance, account_number))
                self.db.conn.commit()
                return True
            else:
                return False
        else:
            return False
        


class TestUserFunctions(unittest.TestCase):
    def setUp(self):
        # Initialize UserFunctions for testing.
        self.user_functions = UserFunctions()

    def test_create_user(self):
        # Test the create_user method.
        # Create a test user and check if it exists in the database.
        self.user_functions.create_user("123456789", "123456", "John", "Doe", 1000.00, "john.doe@example.com", "1234567890", "1990-01-01")
        user_info = self.user_functions.get_user_info("john.doe@example.com")
        self.assertIsNotNone(user_info)
        self.assertEqual(user_info["first_name"], "John")

    def test_authenticate(self):
        # Test the authenticate method.
        # Check if a user with valid credentials can authenticate successfully.
        self.assertTrue(self.user_functions.authenticate("hi@gmail.com", "123456"))

    def test_check_balance(self):
    # Test the check_balance method.
    # Check if the balance of a user is correctly retrieved from the database.
        balance = self.user_functions.check_balance("3.00")
        print("Retrieved balance:", balance)



if __name__ == '__main__':
    unittest.main()

