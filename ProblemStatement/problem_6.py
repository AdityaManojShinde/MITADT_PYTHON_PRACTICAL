# Problem Statement 6: Define a BankAccount class with:Attributes: account_number, balance 
# (private), and name.   
# Methods: Getter and setter for balance (with validation to prevent negative balance).  
# A deposit() method to add money. A withdraw() method to withdraw money (check if sufficient 
# balance exists).

class BankAccount:
    def __init__(self, account_number, balance, name):
        self.account_number = account_number
        self.__balance = balance
        self.name = name
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance < 0:
            print("Balance cannot be negative")
        else:
            self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            return self.__balance
        
    def display_info(self):
        print("\nAccount Information")
        print(f"Account Number: {self.account_number}\nName: {self.name}\nBalance: {self.__balance}")

# Example Usage
acc1 = BankAccount(12345, 1000, "Alice")
acc1.display_info()  

print(acc1.deposit(500))  # Output: 1500
print(acc1.withdraw(200))  # Output: 1300
print(acc1.withdraw(1500))  # Output: Insufficient balance
acc1.display_info()