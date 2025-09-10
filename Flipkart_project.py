from Flipkart_DB import DB

class Flipkart:
    def __init__(self):
        self.DB = DB()
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
=============================
    FLIPKART MAIN MENU
=============================
1. Register
2. Login
3. Exit
Enter your choice: """)

            if user_input == '1':
                self.register()
            elif user_input == '2':
                self.login()
            elif user_input == '3':
                print("🙏 Thank you for visiting Flipkart. Bye! 👋")
                break
            else:
                print("❌ Invalid choice. Please try again.")

    def register(self):
        print("\n=== User Registration ===")
        id = input("Enter ID: ")
        username = input("Enter Username: ")
        password = input("Enter Password (numbers only): ")
        email = input("Enter Email: ")

        self.DB.register(id, username, password, email)

    def login(self):
        print("\n=== User Login ===")
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        success = self.DB.login(username, password)
        if success:
            self.dashboard(username)
        else:
            print("⚠ Login failed! Please try again.")

    def dashboard(self, username):
        while True:
            print(f"""
=============================
    FLIPKART DASHBOARD
=============================
Welcome, {username} 🎉

1. Home 🏠
2. Categories (Mobiles, Electronics, Fashion, etc.)
3. My Cart 🛒
4. My Orders 📦
5. Logout
""")
            after_input = input("Enter your choice: ")

            if after_input == '1':
                print("\n=== 🏠 Home Page ===")
                print("📢 Latest Offers: Mobiles up to 50% OFF!")
            elif after_input == '2':
                print("\n=== 📂 Categories ===")
                print("Mobiles, Electronics, Fashion, Home Appliances, Books, etc.")
            elif after_input == '3':
                print("\n=== 🛒 My Cart ===")
                print("Your cart is empty. Add some products!")
            elif after_input == '4':
                print("\n=== 📦 My Orders ===")
                print("You haven't placed any orders yet.")
            elif after_input == '5':
                confirm = input("Are you sure you want to logout? (yes/no): ").lower()
                if confirm == "yes":
                    print("\n✅ Successfully logged out. Bye!")
                    break
            else:
                print("❌ Invalid choice. Please try again.")


# Start the Flipkart application
if __name__ == "__main__":
    Flipkart()
