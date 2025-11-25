from ATM_DB import ATM_db


class ATM:
    def __init__(self):
        self.db = ATM_db()
        self.account = None  # Will hold logged-in account info

    def main_menu(self):
        while True:
            print("""
ATM Main Menu:
1. Register New User & Account
2. Login to Account
3. Exit
""")
            choice = input("Enter choice: ")
            if choice == '1':
                self.register()
            elif choice == '2':
                self.login()
            elif choice == '3':
                print("Thank you for using ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def register(self):
        name = input("Enter your full name: ")
        email = input("Enter your email address: ")
        mobile = input("Enter your mobile number: ")
        dob = input("Enter your DOB (YYYY-MM-DD): ")
        address = input("Enter your address: ")
        user_id = self.db.create_user(name, email, mobile, dob, address)
        if user_id == -1:
            print("Failed to create user.")
            return

        account_number = input("Set your unique account number: ")
        pin = input("Set a 4-digit PIN: ")
        if len(pin) != 4 or not pin.isdigit():
            print("Invalid PIN format.")
            return
        account_id = self.db.create_account(user_id, account_number, pin)
        if account_id == -1:
            print("Failed to create account.")
        else:
            print("Registration successful! You may now log in.")

    def login(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        account = self.db.verify_account(account_number, pin)
        if not account:
            print("Invalid credentials.")
            return
        self.account = account
        print(f"Welcome, {self.account_number_info()}.")
        self.account_menu()

    def account_number_info(self):
        return self.account.get('account_number') if self.account else "Unknown"

    def account_menu(self):
        while True:
            balance = self.db.get_balance(self.account['account_id'])
            print(f"""
Account Menu (Account #{self.account['account_number']}):
Current Balance: {balance}
1. Deposit Money
2. Withdraw Money
3. Logout
""")
            choice = input("Choose an option: ")
            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.account = None
                print("Logged out.")
                break
            else:
                print("Invalid option.")

    def deposit(self):
        amount = input("Enter deposit amount: ")
        if not amount.isdigit() or int(amount) <= 0:
            print("Enter a valid positive amount.")
            return
        amount = int(amount)
        if self.db.update_balance(self.account['account_id'], amount):
            self.db.record_transaction(self.account['account_id'], 'Deposit', amount)
            print(f"Deposited {amount} successfully.")
        else:
            print("Failed to deposit.")

    def withdraw(self):
        amount = input("Enter withdrawal amount: ")
        if not amount.isdigit() or int(amount) <= 0:
            print("Enter a valid positive amount.")
            return
        amount = int(amount)

        current_balance = self.db.get_balance(self.account['account_id'])
        if amount > current_balance:
            print("Insufficient funds.")
            return

        if self.db.update_balance(self.account['account_id'], -amount):
            self.db.record_transaction(self.account['account_id'], 'Withdraw', amount)
            print(f"Withdrew {amount} successfully.")
        else:
            print("Failed to withdraw.")


if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()
