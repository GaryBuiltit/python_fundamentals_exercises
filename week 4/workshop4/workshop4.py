
from unicodedata import name


# task 1 - function that creates a new user
class User():
    def __init__(self, name: str, pin: int, password):
        self.name = name
        self.pin = pin
        self.password = password

    # task 2 - method to change the password
    def Change_password(self, newPassword):
        self.password = newPassword
        print("Password has been changed to:", self.password)

    # task 2 - method to chanhe tthe username that requires a string input
    def Change_User_Name(self, newUserName: str):
        self.name = newUserName
        print("Username has been changed to:", self.name)

    # task 2 - method to change the user password
    def Change_Pin(self, newPin: int):
        self.pin = newPin
        print("Your pin has been changed to:", self.pin)


# task 3 - function to create a bank user that inherites from the user class
class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

# task 4 - methods that shows users current balance
    def show_balance(self):
        print(f"Your current balance is: ${self.balance}")


# task 4 - method that withdraws funds from users account

    def withdraw(self, amount: float):
        newBalance = self.balance - amount
        self.balance = newBalance
        print("Withdraw Completed")
        print(f"Current balance is: ${self.balance}")


# task 4 - method that depsosits funds into users account

    def deposit(self, amount):
        newBalance = self.balance + amount
        self.balance = newBalance
        print("Deposit Comppleted!")
        print(f"Current balance is: ${self.balance}")


# task 5 - transfers money to another user

    def transfer_money(self, amount, user):
        print(f"You are transferring ${amount} to {user.name}")
        print("Authentication is required")
        pin_check = int(input("Enter your pin: "))
        if self.balance > amount:
            if pin_check == self.pin:
                print("Transferred authorized")
                senders_new_Balance = self.balance - amount
                self.balance = senders_new_Balance
                receivers_new_balance = user.balance + amount
                user.balance = receivers_new_balance
                print(f"Tranferring ${amount} to {user.name}")
                print(f"Your cureent balance is: ${self.balance}")
                print(f"{user.name} current balance is: ${user.balance}")
            else:
                print("Incorrect pin. Transaction cancelled")
        else:
            print("Insufficient funds. Transaction cancelled")


# task 5 - request money from another user

    def request_money(self, amount, user):
        print(f"Your requesting {amount} from {user.name}")
        print(f"{user.name}'s authorization required... ")
        if user.pin != int(input(f"Enter {user.name}'s pin: ")):
            print("Incorrect pin. Transaction cancelled")
        else:
            if self.password == input("Enter your password: "):
                print("Request authorized")
                senders_new_balance = user.balance - amount
                user.balance = senders_new_balance
                requester_new_balance = self.balance + amount
                self.balance = requester_new_balance
                print(f"{user.name} sent ${amount}")
                print(f"{self.name}'s current balance is: ${self.balance}")
                print(f"{user.name}'s current balance is: ${user.balance}")
            else:
                print("incorrect password. Transaction cancelled")


# """ Driver Code for Task 4"""
# user1 = BankUser("Gary", 1234, "password")
# user2 = BankUser("Bob", 1234, "password")
# user1.deposit(500)
# user1.show_balance()
# user1.transfer_money(200, user2)

# user2.request_money(100, user1)
# user1.show_balance()
# user2.show_balance()


# """ Driver Code for Task 4"""
# user1 = BankUser("Gary", 1234, "password")
# user1.show_balance()
# user1.deposit(500)
# user1.show_balance()
# user1.withdraw(250)
# user1.show_balance()


# """ Driver Code for Task 3"""
# user1 = BankUser("Gary", 1234, "password")
# print(user1.name, user1.pin, user1.password, user1.balance)


# """ Driver Code for Task 2 """
# user1 = User("Gary", 1234, "password")
# print(user1.name, user1.pin, user1.password)
# user1.Change_User_Name("Gary Alford")
# user1.Change_Pin(5678)
# user1.Change_password("new password")
# print(user1.name, user1.pin, user1.password)


# """ Driver Code for Task 1 """
# user1 = User("Gary", 1234, "password")
# print(user1.name, user1.pin, user1.password)
