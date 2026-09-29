# Bank account class :
class BankAccount:
    
    def __init__(self):
        self.balance = 0  
        print("Welcome to the Machine")

    # Deposit method :
    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print(f"\nAmount Deposited: {amount}")

    # Withdraw method :
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print(f"\nYou Withdrew: {amount}")
        else:
            print("\nInsufficient balance")

    # Display method :
    def display(self):
        print(f"\nNet Available Balance = {self.balance}")


my_account = BankAccount()

my_account.deposit()
my_account.withdraw()
my_account.display()