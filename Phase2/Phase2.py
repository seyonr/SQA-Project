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
                        # This line will be replaced with what will happen in the backend
                        print("Withdrawal successful for backend!")
                    
                    # This will handle another withdrawal input from user
                    restart_input = input("Would you like to make another withdrawal? (yes/no): ").strip().lower()
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

                if(withdrawal_amount > 500):
                    print("Standard users can’t withdraw above 500, session terminated!")
                    exit()
                elif(withdrawal_amount > accounts[self.current_user].balance):
                    print("Insufficient balance, session terminated!")
                    exit()
                else:
                    # This line will be replaced with what will happen in the backend
                        print("Withdrawal successful for backend!")

                restart_input = input("Would you like to make another withdrawal? (yes/no): ").strip().lower()
                if restart_input.lower() != "yes":
                    break


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
                    action = input("\nWhat do you want to do today?\nW – Withdrawal\nL – Logout\n").strip().lower()
                    if action == "w": # Withdrawal handle
                        withdrawal_instance = Withdrawal(self.current_account)
                        withdrawal_instance.process()
                    
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