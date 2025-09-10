import mysql.connector
import sys

class DB:
    def __init__(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                database="practicedatabase",  # Your DB name
                user="root",
                password=""
            )
            self.cursor = self.db.cursor()
        except mysql.connector.Error as e:
            print("Database connection failed ❌:", e)
            sys.exit()
        else:
            print("✅ Database connection successful!")

    # Register a new user
    def register(self, id, username, password, email):
        try:
            self.cursor.execute('''
                INSERT INTO practicedatabase (id, username, password, email)
                VALUES (%s, %s, %s, %s)
            ''', (id, username, int(password), email))
            self.db.commit()
            print("✅ Registration successful!")
        except mysql.connector.Error as e:
            print("Registration failed ❌:", e)

    # Login verification
    def login(self, username, password):
        try:
            self.cursor.execute(
                "SELECT * FROM practicedatabase WHERE username = %s AND password = %s",
                (username, int(password))
            )
            result = self.cursor.fetchone()
            if result:
                print(f"✅ Login successful! Welcome, {result[1]}")
                return True
            else:
                print("❌ Invalid username or password.")
                return False
        except mysql.connector.Error as e:
            print("Login failed ❌:", e)
            return False
