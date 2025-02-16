
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            print("Withdrawal amount must be greater than zero.")

    def check_balance(self):
        print(f"Account Number: {self.account_number}, Balance: ₹{self.balance}")


account = BankAccount("123456789", 5000) 
account.check_balance()

account.deposit(2000)  
account.withdraw(1500) 
account.withdraw(7000)  
account.check_balance()  
