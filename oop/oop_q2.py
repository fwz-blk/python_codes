# BankAccount Class
# Attributes:
# account_holder (string)
# balance (float)

# Methods:
# deposit(amount) → adds amount to balance
# withdraw(amount) → subtracts amount from balance if sufficient funds
# display() → prints account holder and current balance

# Task:
# Create account "Fawaz" with balance 1000
# Deposit 500
# Withdraw 300
# Display account holder and current balance

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if(amount <= self.balance):
            self.balance=self.balance-amount
        else:
            print(f"Insufficient funds! balance={self.balance}")
    
    def display(self):
        print(f"Account Holder :{self.name}")
        print(f"Balance Left : {self.balance}")


F=BankAccount("Fawaz",1000)

F.display()
F.deposit(500)
F.withdraw(300)
F.display()

        
