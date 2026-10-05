class BankAccount :
    def __init__(self):
        self.balance = 0
        print(f"Welcome to the Machine")

    # Amount Deposit method :
    def amount_deposit(self) :
        money_deposit = float(input("\nEnter amount to be deposited : "))
        print(f"{money_deposit:.2f} deposited to your account.")
        self.balance += money_deposit

    # Withdraw money method :
    def withdraw_amount(self) :
        withdraw_money = float(input("\nEnter amount to withdraw : "))
        if withdraw_money < self.balance :
            print(f"{withdraw_money:.2f} withdrawn from your account.")
            self.balance -= withdraw_money
        else : 
            print("\nInsufficient balance.")

    # Total ammount :
    def __str__(self):
        return(f"\nNet Available Balance : {self.balance:.2f}")

my_account = BankAccount()
my_account.amount_deposit()
my_account.withdraw_amount()
print(my_account)
