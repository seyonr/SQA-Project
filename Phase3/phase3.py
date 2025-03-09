# Dummy accounts dictionary for testing purposes.
accounts = {
    12345: type("Account", (), {"name": "John Bob", "balance": 1000, "account_type": "admin"}),
    54321: type("Account", (), {"name": "Jane Doe", "balance": 500, "account_type": "standard"}),
    00000: type("Account", (), {"name": "Ana Bob", "balance": 100, "account_type": "standard"}),
    99999: type("Account", (), {"name": "Bill Gates", "balance": 500000, "account_type": "standard"}),
}

# Class which handles login
class Login:
    def __init__(self, login_type, number, name):
        self.login_type = login_type
        self.number = number
        self.name = name
        self.current_user = None

    def authenticate(self):
        if self.number in accounts:
            if self.login_type == "standard":
                if accounts[self.number].name == self.name:
                    self.current_user = self.number
                    print("Login successful!")
                    return True
                else:
                    print("Invalid account name, session terminated!")
                    exit()
            else:
                self.current_user = self.number
                print("Login successful!")
                return True
        else:
            print("Invalid account number, session terminated!")
            exit()


# Class which handles withdrawal
class Withdrawal:
    def __init__(self, current_user):
        self.current_user = current_user

    def process(self):
        while True:
            # Handles admin withdrawal
            if accounts[self.current_user].account_type == "admin":
                from_num = int(input("Please enter the account number you want to withdraw from : \n"))  
                from_name = input("Please enter the account name you want to withdraw from : \n")  

                if (from_num in accounts) and (accounts[from_num].name == from_name):
                    withdrawal_amount = int(input("How much would you like to withdraw : \n"))  

                    if withdrawal_amount > accounts[from_num].balance:
                        print("Insufficient balance, session terminated!")
                        exit()
                    else:
                        print("Withdrawal successful for backend!")  # This will be replaced with backend logic

                    restart_input = input("Would you like to make another withdrawal : \n").strip().lower()  
                    if restart_input.lower() != "yes":
                        break

                elif not (from_num in accounts):
                    print("Invalid account number, session terminated!")
                    exit()

                else:
                    print("Invalid account name, session terminated!")
                    exit()

            # Handles standard withdrawal
            else:
                withdrawal_amount = int(input("How much would you like to withdraw : \n"))  

                if withdrawal_amount > 500:
                    print("Standard users can’t withdraw above 500, session terminated!")
                    exit()
                elif withdrawal_amount > accounts[self.current_user].balance:
                    print("Insufficient balance, session terminated!")
                    exit()
                else:
                    print("Withdrawal successful for backend!")  # This will be replaced with backend logic

                restart_input = input("Would you like to make another withdrawal : \n").strip().lower()  
                if restart_input.lower() != "yes":
                    break


# Class which handles transfer
class Transfer:
    def __init__(self, current_user):
        self.current_user = current_user

    def process(self):
        while True:
            # Handles admin transfer
            if accounts[self.current_user].account_type == "admin":
                from_num = int(input("Please enter the account number you want to transfer from : \n"))  
                from_name = input("Please enter the account name you want to transfer from : \n")  
                to_num = int(input("Please enter the account number you want to transfer to : \n"))  

                if (from_num in accounts) and (accounts[from_num].name == from_name) and (to_num in accounts):
                    transfer_amount = int(input("How much would you like to transfer : \n"))  

                    if transfer_amount > accounts[from_num].balance:
                        print("Insufficient balance, session terminated!")
                        exit()
                    else:
                        print("Transfer successful for backend")  # This will be replaced with backend logic

                    restart_input = input("Transfer successful, would you like to to make another transfer : \n").strip().lower() 
                    if restart_input.lower() != "yes":
                        break

                elif not (from_num in accounts) or not (to_num in accounts):
                    print("Invalid account number, session terminated!")
                    exit()

                else:
                    print("Invalid account name, session terminated!")
                    exit()

            # Handles standard transfer
            else:
                to_num = int(input("Please enter the account number you want to transfer to : \n"))  

                if to_num in accounts:
                    transfer_amount = int(input("How much would you like to transfer : \n"))  

                    if transfer_amount > 1000:
                        print("Standard users can’t transfer above 1000! ")
                        exit()
                    elif transfer_amount > accounts[self.current_user].balance:
                        print("Insufficient balance, session terminated!")
                        exit()
                    else:
                        print("Transfer successful for backend")  # This will be replaced with backend logic

                    restart_input = input("Transfer successful, would you like to to make another transfer : \n").strip().lower()  
                    if restart_input.lower() != "yes":
                        break

                else:
                    print("Invalid account number, session terminated!")
                    exit()


# Class which handles paybill
class PayBill:
    def __init__(self, current_user):
        self.current_user = current_user

    def process(self):
        while True:
            # Handles admin paybill
            if accounts[self.current_user].account_type == "admin":
                from_num = int(input("Please enter the account number you want to transfer from : \n"))  
                from_name = input("Please enter the account name you want to transfer from : \n")  

                if (from_num in accounts) and (accounts[from_num].name == from_name):
                    payee = input("Please select the payee you want to pay the bill to:\nEC - The Bright Light Electric Company\nCQ - Credit Card Company Q\nFI - Fast Internet, Inc.\n").strip().lower()  
                    if payee in ("ec", "cq", "fi"):
                        pay_amount = int(input("How much would you like to pay : \n"))  
                        if pay_amount > accounts[from_num].balance:
                            print("Insufficient balance, session terminated!")
                            exit()
                        else:
                            print("Payment successful for backend ")  # This will be replaced with backend logic

                        restart_input = input("Payment successful, would you like to to make another payment : \n").strip().lower()  
                        if restart_input.lower() != "yes":
                            break

                    else:
                        print("Invalid payee, session terminated!")
                        exit()
                elif not (from_num in accounts):
                    print("Invalid account number, session terminated!")
                    exit()
                else:
                    print("Invalid account name, session terminated!")
                    exit()

            # Handles standard paybill
            else:
                payee = input("Please select the payee you want to pay the bill to:\nEC - The Bright Light Electric Company\nCQ - Credit Card Company Q\nFI - Fast Internet, Inc.\n").strip().lower()  

                if payee in ("ec", "cq", "fi"):
                    pay_amount = int(input("How much would you like to pay : \n"))  
                    if pay_amount > 2000:
                        print("Standard users can’t pay bills above 2000! ")
                        exit()
                    elif pay_amount > accounts[self.current_user].balance:
                        print("Insufficient balance, session terminated!")
                        exit()
                    else:
                        print("Payment successful for backend ")  # This will be replaced with backend logic

                    restart_input = input("Payment successful, would you like to to make another payment : \n").strip().lower()  
                    if restart_input.lower() != "yes":
                        break

                else:
                    print("Invalid payee, session terminated!")
                    exit()


# Class which handles deposit
class Deposit:
    def __init__(self, current_user):
        self.current_user = current_user

    def process(self):
        while True:
            # Handles admin deposit
            if accounts[self.current_user].account_type == "admin":
                from_num = int(input("Please enter the account number you want to deposit to : \n"))  
                from_name = input("Please enter the account name you want to deposit to : \n")  

                if (from_num in accounts) and (accounts[from_num].name == from_name):
                    deposit_amount = int(input("How much would you like to deposit : \n"))  

                    print("Deposit successful for backend:")  # This will be replaced with backend logic

                    restart_input = input("Deposit successful, would you like to to make another deposit :  \n").strip().lower()  
                    if restart_input.lower() != "yes":
                        print("Logged out!")
                        print("Have a great day, see you soon!")
                        exit()
                elif not (from_num in accounts):
                    print("Invalid account number, session terminated!")
                    exit()
                else:
                    print("Invalid account name, session terminated!")
                    exit()

            # Handles standard deposit
            else:
                deposit_amount = int(input("How much would you like to deposit : \n"))  

                print("Deposit successful for backend:")  # This will be replaced with backend logic

                restart_input = input("Deposit successful, would you like to to make another deposit :  \n").strip().lower()  
                if restart_input.lower() != "yes":
                    print("Logged out!")
                    print("Have a great day, see you soon!")
                    exit()


# Class which handles creating accounts
class Create:
    def __init__(self, current_user):
        self.current_user = current_user

    def process(self):
        while True:
            # Handles admin creating account
            if accounts[self.current_user].account_type == "admin":
                new_num = int(input("Please enter a new account number : \n"))  
                new_name = input("Please enter a new account name : \n")  
                initial_balance = float(input("Please enter initial balance : \n"))  

                if new_num in accounts:
                    print("Duplicate account number, session terminated!")
                    exit()
                elif len(new_name) > 20:
                    print("Account name can’t be longer than 20 characters, session terminated!")
                    exit()
                elif initial_balance > 99999.99:
                    print("Balance can’t be above $99999.99, session terminated!")
                    exit()
                else:
                    print("New account created successfully, session terminated!")  # This will be replaced with backend logic
                    exit()

            # Handles standard user trying to creating account
            else:
                print("Permission denied, session terminated!")
                exit()


# Class which handles deleting accounts
class Delete:
    def __init__(self, current_user):
        self.current_user = current_user

    def process(self):
        while True:
            # Handles admin delete
            if accounts[self.current_user].account_type == "admin":
                delete_num = int(input("Please enter the account number of the account to delete : \n"))  
                delete_name = input("Please enter the account name of the account to delete : \n")  

                if not (delete_num in accounts):
                    print("Invalid account number, session terminated! ")
                    exit()
                elif accounts[delete_num].name != delete_name:
                    print("Invalid account name, session terminated! ")
                    exit()
                else:
                    print("Account deleted successfully, session terminated!")  # This will be replaced with backend logic
                    exit()
            else:
                print("Permission denied, session terminated!")
                exit()


# Class which handles disable of accounts
class Disable:
    def __init__(self, current_user):
        self.current_user = current_user

    def process(self):
        while True:
            # Handles admin disable
            if accounts[self.current_user].account_type == "admin":
                disable_num = int(input("Please enter the account number of the account to disable : \n"))  
                disable_name = input("Please enter the account name of the account to disable : \n")  

                if not (disable_num in accounts):
                    print("Invalid account number, session terminated! ")
                    exit()
                elif accounts[disable_num].name != disable_name:
                    print("Invalid account name, session terminated! ")
                    exit()
                else:
                    print("Account disabled successfully, session terminated!")  # This will be replaced with backend logic
                    exit()
            else:
                print("Permission denied, session terminated!")
                exit()


# Class which handles changeplan
class ChangePlan:
    def __init__(self, current_user):
        self.current_user = current_user

    def process(self):
        # Handles admin change plan
        if accounts[self.current_user].account_type == "admin":
            change_num = int(input("Please enter the account number of the account to change plan for : \n"))  
            change_name = input("Please enter the account name of the account to change plan for : \n")  

            if not (change_num in accounts):
                print("Invalid account number, session terminated!")
                exit()
            elif accounts[change_num].name != change_name:
                print("Invalid account name, session terminated!")
                exit()
            else:
                print("Account changed from student plan to non-student plan successfully, session terminated!")  # This will be replaced with backend logic
                exit()
        else:
            print("Permission denied, session terminated!")
            exit()


# Class which handles overall bank system
class BankSystem:
    def __init__(self):
        self.current_account = None

    def main(self):
        print("Welcome to the banking system!")
        start_input = input("Do you want to login or exit : \n").strip().lower()  

        if start_input != "exit":
            login_type = input("Enter login type (admin or standard): \n").strip().lower()  
            number_input = int(input("Enter account number: \n"))

            if login_type == "standard":
                name_input = input("Enter account name: \n")  # Ex. John Bob
                login_instance = Login(login_type, number_input, name_input)
            else:
                login_instance = Login(login_type, number_input, "admin")

            if login_instance.authenticate():
                self.current_account = login_instance.current_user

                while True:
                    action = input("\nWhat do you want to do today?\nW – Withdrawal\nT - Transfer\nP - Paybill\nD - Deposit\nC - Create\nDE - Delete\nDI - Disable\nCH - Change Plan\nL – Logout\n").strip().lower() 
                    if action == "w":
                        withdrawal_instance = Withdrawal(self.current_account)
                        withdrawal_instance.process()

                    elif action == "t":
                        transfer_instance = Transfer(self.current_account)
                        transfer_instance.process()

                    elif action == "p":
                        paybill_instance = PayBill(self.current_account)
                        paybill_instance.process()

                    elif action == "d":
                        deposit_instance = Deposit(self.current_account)
                        deposit_instance.process()

                    elif action == "c":
                        create_instance = Create(self.current_account)
                        create_instance.process()

                    elif action == "de":
                        delete_instance = Delete(self.current_account)
                        delete_instance.process()

                    elif action == "di":
                        disable_instance = Disable(self.current_account)
                        disable_instance.process()

                    elif action == "ch":
                        change_instance = ChangePlan(self.current_account)
                        change_instance.process()

                    elif action == "l":
                        print("Logged out!")
                        print("Have a great day, see you soon!")
                        self.current_account = None
                        break

                    else:
                        print("Invalid command.")
        else:
            print("Have a great day, see you soon!")


if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.main()