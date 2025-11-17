


"""
Exercise 1: Identify and Correct Naming Violations
The following Python code snippet has several naming convention violations. Your task is to refactor it to comply with PEP 8.

Your Task:

Go through each variable, function, method, and class name.
Determine if it adheres to PEP 8 naming conventions.
If not, rename it to the correct convention.
Apply other basic PEP 8 style guidelines (e.g., blank lines, whitespace) where appropriate.
"""


# Code with naming violations
global_Tax_Rate = 0.05

class userAccount:
    def __init__(self, userName, user_ID):
        self.userName = userName
        self.User_ID = user_ID
        self.ACCOUNT_BALANCE = 0.0

    def addTransaction(self, amount):
        if amount > 0:
            self.ACCOUNT_BALANCE += amount
            print(f"Added {amount}. New balance: {self.ACCOUNT_BALANCE}")
        else:
            print("Transaction amount must be positive.")

    def calculateInterest(self, Rate):
        interest = self.ACCOUNT_BALANCE * Rate
        self.ACCOUNT_BALANCE += interest
        return interest

def printUserDetail(account):
    print(f"User: {account.userName}, ID: {account.User_ID}, Balance: {account.ACCOUNT_BALANCE}")

# Usage
myUser = userAccount("johnDoe", "JD123")
myUser.addTransaction(100)
myUser.addTransaction(-50)
myUser.calculateInterest(0.01)
printUserDetail(myUser)