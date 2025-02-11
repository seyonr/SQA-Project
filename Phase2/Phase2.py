# Class to hold info about accounts 
class Account:
    def __init__(self, num, name, balance, account_type):
        self.num = num
        self.name = name
        self.balance = balance
        self.account_type = account_type

# Hard set accounts for the purpose of basic testing
# In the future, the backend will populate the accounts dictonary
accounts = {
    12345: Account(12345, "John Bob", 500, "standard"),
    11111: Account(11111, "James Bond", 200, "standard"),
    54321: Account(54321, "admin", 99999, "admin")
}



# Class which handles login
class Login:
    # Constructor 
    def __init__(self, login_type, acc_num, acc_name):
        self.login_type = login_type
        self.acc_num = acc_num
        self.acc_name = acc_name
        self.current_user = None

    # Function to authenticate login
    def authenticate(self):
        # Handles admin login
        if(self.login_type == "admin"):
            if(self.acc_num in accounts and accounts[self.acc_num].account_type == "admin"): # Handles successful admin login
                self.current_user = self.acc_num
                print(f"Logged in as admin!")
                return True
            else: # Handles incorrect account number
                print("Invalid account number, session terminated!")
                return False
            
        # Handles standard user login 
        elif(self.login_type == "standard"): 
            if((self.acc_num in accounts) and (accounts[self.acc_num].name == self.acc_name)): # Handles successful standard login
                self.current_user = self.acc_num
                print("Logged in as standard!")
                return True
            elif(not(self.acc_num in accounts)): # Handles incorrect account number
                print("Invalid account number, session terminated!")
                return False
            else: # Handles incorrect account name
                print("Invalid account name, session terminated!")
                return False

        else: # Handles unexpected error for login
            print("Error with login, session terminated!")
            return False



# Class which handles withdrawal
class Withdrawal:
    # Constructor 
    def __init__(self, current_user):
        self.current_user = current_user

    # Function to process withdrawal
    def process(self):
        while True:
            # Handles admin withdrawal
            if(accounts[self.current_user].account_type == "admin"):
                from_num = int(input("Please enter the account number you want to withdraw from : "))
                from_name = input("Please enter the account name you want to withdraw from : ")

                if((from_num in accounts) and (accounts[from_num].name == from_name)): # Handles successful admin input
                    withdrawal_amount = int(input("How much would you like to withdraw : "))

                    if(withdrawal_amount > accounts[from_num].balance): # Handles insufficient balance
                        print("Insufficient balance, session terminated!")
                        exit()
                    else: # Handles successful withdrawal
                        print("Withdrawal successful for backend!") # This will be replaced with backend logic
                    
                    # This will handle another withdrawal input from user
                    restart_input = input("Would you like to make another withdrawal : ").strip().lower()
                    if restart_input.lower() != "yes":
                        break
                            
                elif(not(from_num in accounts)): # Handles incorrect account number
                    print("Invalid account number, session terminated!")
                    exit()

                else: # Handles incorrect account name
                    print("Invalid account name, session terminated!")
                    exit()
            
            # Handles standard withdrawal
            else:
                withdrawal_amount = int(input("How much would you like to withdraw : "))

                if(withdrawal_amount > 500): # Handles standard user limit
                    print("Standard users can’t withdraw above 500, session terminated!")
                    exit()
                elif(withdrawal_amount > accounts[self.current_user].balance): # Handles insufficient balance
                    print("Insufficient balance, session terminated!")
                    exit()
                else: # Handles sucessful withdrawal
                        print("Withdrawal successful for backend!") # This will be replaced with backend logic

                restart_input = input("Would you like to make another withdrawal : ").strip().lower()
                if restart_input.lower() != "yes":
                    break



# Class which handles transfer
class Transfer:
    # Constructor 
    def __init__(self, current_user):
        self.current_user = current_user

    # Function to process transfer
    def process(self):
        while True:
            # Handles admin transfer
            if(accounts[self.current_user].account_type == "admin"):
                from_num = int(input("Please enter the account number you want to transfer from : "))
                from_name = input("Please enter the account name you want to transfer from : ")
                to_num = int(input("Please enter the account number you want to transfer to : "))

                if((from_num in accounts) and (accounts[from_num].name == from_name) and (to_num in accounts)): # Handles successful admin input
                    transfer_amount = int(input("How much would you like to transfer : "))

                    if(transfer_amount > accounts[from_num].balance): # Handles insufficient balance
                        print("Insufficient balance, session terminated!")
                        exit()
                    else: # Handles sucessful transfer
                        print("Transfer successful for backend") # This will be replaced with backend logic
                
                    # Handles another transfer request
                    restart_input = input("Transfer successful, would you like to to make another transfer : ").strip().lower()
                    if restart_input.lower() != "yes":
                        break
                
                elif(not(from_num in accounts) or not(to_num in accounts)): # Handles incorrect account number
                    print("Invalid account number, session terminated!")
                    exit()

                else: # Handles incorrect account name
                    print("Invalid account name, session terminated!")
                    exit()

            # Handles standard transfer
            else:
                to_num = int(input("Please enter the account number you want to transfer to : "))

                if(to_num in accounts): # Handles correct transfer account number
                    transfer_amount = int(input("How much would you like to transfer : "))

                    if(transfer_amount > 1000): # Handles standard user limit
                        print("Standard users can’t transfer above 1000! ")
                        exit()
                    elif(transfer_amount > accounts[self.current_user].balance): # Handles insufficient balance
                        print("Insufficient balance, session terminated!")
                        exit()
                    else: # Handles sucessful transfer
                        print("Transfer successful for backend") # This will be replaced with backend logic
                    
                    # Handles another transfer request 
                    restart_input = input("Transfer successful, would you like to to make another transfer : ").strip().lower()
                    if restart_input.lower() != "yes":
                        break

                else: # Handles incorrect transfer account number
                    print("Invalid account number, session terminated!")
                    exit()



# Class which handles paybill
class Paybill:
    # Constructor 
    def __init__(self, current_user):
        self.current_user = current_user

    # Function to process paybill
    def process(self):
        while True:
            # Handles admin paybill
            if(accounts[self.current_user].account_type == "admin"):
                from_num = int(input("Please enter the account number you want to transfer from : "))
                from_name = input("Please enter the account name you want to transfer from : ")

                if((from_num in accounts) and (accounts[from_num].name == from_name)): # Handles successful admin input
                    payee = input("Please select the payee you want to pay the bill to:\nEC - The Bright Light Electric Company\nCQ - Credit Card Company Q\nFI - Fast Internet, Inc.\n").strip().lower()
                    if((payee == "ec") or (payee == "cq") or (payee == "fi")): # Handles sucessfull payee selection 
                        pay_amount = int(input("How much would you like to pay : "))
                        if(pay_amount > accounts[from_num].balance): # Handles insufficient balance
                            print("Insufficient balance, session terminated!")
                            exit()
                        else: # Handles sucessful transfer
                            print("Payment successful for backend ") # This will be replaced with backend logic

                        # Handles another payment request 
                        restart_input = input("Payment successful, would you like to to make another payment : ").strip().lower()
                        if restart_input.lower() != "yes":
                            break

                    else: # Handles invalid payee selection 
                        print("Invalid payee, session terminated!")
                        exit()
                elif(not(from_num in accounts)): # Handles incorrect account number
                    print("Invalid account number, session terminated!")
                    exit()
                else: # Handles incorrect account name
                    print("Invalid account name, session terminated!")
                    exit()

            # Handles standard paybill
            else:
                payee = input("Please select the payee you want to pay the bill to:\nEC - The Bright Light Electric Company\nCQ - Credit Card Company Q\nFI - Fast Internet, Inc.\n").strip().lower()
                
                if((payee == "ec") or (payee == "cq") or (payee == "fi")): # Handles sucessfull payee selection 
                    pay_amount = int(input("How much would you like to pay : "))
                    if(pay_amount > 2000): # Handles standard user limit
                        print("Standard users can’t pay bills above 2000! ")
                        exit()
                    elif(pay_amount > accounts[self.current_user].balance): # Handles insufficient balance
                        print("Insufficient balance, session terminated!")
                        exit()
                    else: # Handles sucessful transfer
                        print("Payment successful for backend ") # This will be replaced with backend logic

                    # Handles another payment request 
                    restart_input = input("Payment successful, would you like to to make another payment : ").strip().lower()
                    if restart_input.lower() != "yes":
                        break
                
                else: # Handles invalid payee selection 
                    print("Invalid payee, session terminated!")
                    exit()



# Class which handles deposit
class Deposit:
    # Constructor 
    def __init__(self, current_user):
        self.current_user = current_user

    # Function to process deposit
    def process(self):
        while True:
            # Handles admin deposit
            if(accounts[self.current_user].account_type == "admin"):
                from_num = int(input("Please enter the account number you want to deposit to : "))
                from_name = input("Please enter the account name you want to deposit to : ")
                
                if((from_num in accounts) and (accounts[from_num].name == from_name)): # Handles successful input
                    deposit_amount = int(input("How much would you like to deposit : "))
                    
                    print("Deposit successful for backend:") # This will be replaced with backend logic

                    # Handles another deposit request
                    restart_input = input("Deposit successful, would you like to to make another deposit :  ").strip().lower()
                    if restart_input.lower() != "yes":
                        print("Logged out!")
                        print("Have a great day, see you soon!")
                        exit()
                elif(not(from_num in accounts)): # Handles incorrect account number
                    print("Invalid account number, session terminated!")
                    exit()
                else: # Handles incorrect account name
                    print("Invalid account name, session terminated!")
                    exit()

            # Handles standard deposit
            else:
                deposit_amount = int(input("How much would you like to deposit : "))

                print("Deposit successful for backend:") # This will be replaced with backend logic

                # Handles another deposit request
                restart_input = input("Deposit successful, would you like to to make another deposit :  ").strip().lower()
                if restart_input.lower() != "yes":
                    print("Logged out!")
                    print("Have a great day, see you soon!")
                    exit()



# Class which handles creating accounts
class Create:
    # Constructor 
    def __init__(self, current_user):
        self.current_user = current_user

    # Function to process create
    def process(self):
        while True:
            # Handles admin creating account 
            if(accounts[self.current_user].account_type == "admin"):
                new_num = int(input("Please enter a new account number : "))
                new_name = input("Please enter a new account name : ")
                initial_balance = float(input("Please enter initial balance : "))

                if(new_num in accounts): # Handles duplicate account number
                    print("Duplicate account number, session terminated!")
                    exit()
                elif(len(new_name) > 20): # Handles name longer than 20 characters
                    print("Account name can’t be longer than 20 characters, session terminated!")
                    exit()
                elif(initial_balance > 99999.99): # Handles balance set above $99999.99
                    print("Balance can’t be above $99999.99, session terminated!")
                    exit()
                else: # Handles successful creation of account
                    print("New account created successfully, session terminated!") # This will be replaced with backend logic
                    exit()

            # Handles standard creating account 
            else:
                print("Permission denied, session terminated!")
                exit()



# Class which handles deleting accounts
class Delete:
    # Constructor 
    def __init__(self, current_user):
        self.current_user = current_user

    # Function to process delete
    def process(self):
        while True:
            # Handles admin delete
            if(accounts[self.current_user].account_type == "admin"):
                delete_num = int(input("Please enter the account number of the account to delete : "))
                delete_name = input("Please enter the account name of the account to delete : ")

                if(not(delete_num in accounts)): # Handles incorrect account number
                    print("Invalid account number, session terminated! ")
                    exit()
                elif(accounts[delete_num].name != delete_name): # Handles incorrect account name
                    print("Invalid account name, session terminated! ")
                    exit()
                else: # Handles successful input
                    print("Account deleted successfully, session terminated!") # This will be replaced with backend logic
                    exit()
            # Handles standard delete
            else:
                print("Permission denied, session terminated!")
                exit()


 
# Class which handles disable of accounts
class Disable:
    # Constructor 
    def __init__(self, current_user):
        self.current_user = current_user

    def process(self):
        while True:
            # Handles admin disable 
            if(accounts[self.current_user].account_type == "admin"):
                disable_num = int(input("Please enter the account number of the account to disable : "))
                disable_name = input("Please enter the account name of the account to disable : ")

                if(not(disable_num in accounts)):  # Handles incorrect account number
                    print("Invalid account number, session terminated! ")
                    exit()
                elif(accounts[disable_num].name != disable_name):  # Handles incorrect account name
                    print("Invalid account name, session terminated! ")
                    exit()
                else: # Handles sucessful input
                    print("Account disabled successfully, session terminated!") # This will be replaced with backend logic
                    exit()
            # Handles standard disable
            else:
                print("Permission denied, session terminated!")
                exit()






# Class which handles overall bank system
class BankSystem:
    # Constructor 
    def __init__(self):
        self.current_account = None

    # Main function to handle the bank system 
    def main(self):
        start_input = input("Do you want to login or exit : ").strip().lower()
        
        # Code to handle user wanting to login
        if(start_input != "exit"):
            login_type = input("Enter login type (admin or standard): ").strip().lower() 
            number_input = int(input("Enter account number: "))
            
            # If standard login then account name will be asked 
            if(login_type == "standard"):
                name_input = input("Enter account name: ")
                login_instance = Login(login_type, number_input, name_input)
            
            # If admin login, account name won't be asked
            else:
                login_instance = Login(login_type, number_input, "admin")

            # Check if login successful, if so the main transactions will happen
            if login_instance.authenticate():
                self.current_account = login_instance.current_user
                
                while True:
                    action = input("\nWhat do you want to do today?\nW – Withdrawal\nT - Transfer\nP - Paybill\nD - Deposit\nC - Create\nDE - Delete\nDI - Disable\nL – Logout\n").strip().lower()
                    if action == "w": # Withdrawal handle
                        withdrawal_instance = Withdrawal(self.current_account)
                        withdrawal_instance.process()

                    elif action == "t": # Transfer handle
                        transfer_instance = Transfer(self.current_account)
                        transfer_instance.process()

                    elif action == "p":
                        paybill_instance  = Paybill(self.current_account)
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
                    
                    elif action == "l": # Logout handle
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