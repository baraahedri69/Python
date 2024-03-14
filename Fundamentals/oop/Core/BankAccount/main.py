class BankAccount:
    accounts = []

    def __init__(self, int_rate=0.01, balance=0):
        self.balance = balance
        self.interest_rate = int_rate
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self

    @classmethod
    def print_all_accounts_info(cls):
        for account in cls.accounts:
            print(f"Account Balance: ${account.balance}, Interest Rate: {account.interest_rate}")

# Create 2 accounts#
account1 = BankAccount(0.02, 1000)
account2 = BankAccount(0.03)

account1.deposit(300).deposit(500).deposit(200).withdraw(100).yield_interest().display_account_info()

account2.deposit(200).deposit(100).withdraw(50).withdraw(100).withdraw(150).withdraw(50).yield_interest().display_account_info()

BankAccount.print_all_accounts_info()