import sys
import mysql.connector

class ATM_db:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="atm"      # Replace with your DB name
            )
            self.cursor = self.conn.cursor(dictionary=True)
        except mysql.connector.Error as err:
            print("Failed to connect to database:")
            print(err)
            sys.exit()
        else:
            print("Connected to MySQL database.")

    def create_user(self, name, email, mobile, dob, address):
        try:
            self.cursor.execute("""
                INSERT INTO Users (name, email, mobile, dob, address) VALUES (%s, %s, %s, %s, %s)
            """, (name, email, mobile, dob, address))
            self.conn.commit()
            return self.cursor.lastrowid  # user_id
        except mysql.connector.Error as err:
            print(f"Error creating user: {err}")
            return -1

    def create_account(self, user_id, account_number, pin):
        try:
            self.cursor.execute("""
                INSERT INTO Accounts (user_id, account_number, pin, balance) VALUES (%s, %s, %s, %s)
            """, (user_id, account_number, pin, 0))
            self.conn.commit()
            return self.cursor.lastrowid  # account_id
        except mysql.connector.Error as err:
            print(f"Error creating account: {err}")
            return -1

    def verify_account(self, account_number, pin):
        try:
            self.cursor.execute("""
                SELECT * FROM Accounts WHERE account_number=%s AND pin=%s
            """, (account_number, pin))
            account = self.cursor.fetchone()
            return account
        except mysql.connector.Error as err:
            print(f"Error verifying account: {err}")
            return None

    def update_balance(self, account_id, amount_change):
        try:
            # Update balance by amount_change (+deposit, -withdraw)
            self.cursor.execute("""
                UPDATE Accounts SET balance = balance + %s WHERE account_id = %s
            """, (amount_change, account_id))
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error updating balance: {err}")
            return False

    def record_transaction(self, account_id, transaction_type, amount):
        try:
            self.cursor.execute("""
                INSERT INTO Transactions (account_id, transaction_type, amount) VALUES (%s, %s, %s)
            """, (account_id, transaction_type, amount))
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error recording transaction: {err}")
            return False

    def get_balance(self, account_id):
        try:
            self.cursor.execute("SELECT balance FROM Accounts WHERE account_id=%s", (account_id,))
            result = self.cursor.fetchone()
            if result:
                return result['balance']
            return None
        except mysql.connector.Error as err:
            print(f"Error getting balance: {err}")
            return None
