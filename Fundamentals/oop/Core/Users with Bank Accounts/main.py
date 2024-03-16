class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []  

    def add_account(self, int_rate=0.02, balance=0):
        new_account = BankAccount(int_rate, balance)
        self.accounts.append(new_account)
        return self

    def make_deposit(self, account_idx, amount):
        if 0 <= account_idx < len(self.accounts):
            self.accounts[account_idx].deposit(amount)
            print(f"{self.name} deposited ${amount} into Account {account_idx + 1}")
        else:
            print("Invalid account index")

    def make_withdrawal(self, account_idx, amount):
        if 0 <= account_idx < len(self.accounts):
            self.accounts[account_idx].withdraw(amount)
            print(f"{self.name} withdrew ${amount} from Account {account_idx + 1}")
        else:
            print("Invalid account index")

    def display_user_balance(self):
        print(f"{self.name}'s Account Balances:")
        for idx, account in enumerate(self.accounts):
            print(f"Account {idx + 1}: ${account.balance}")

    def transfer_money(self, amount, other_user, from_account_idx, to_account_idx):
        if 0 <= from_account_idx < len(self.accounts) and 0 <= to_account_idx < len(other_user.accounts):
            if self.accounts[from_account_idx].balance >= amount:
                self.accounts[from_account_idx].withdraw(amount)
                other_user.accounts[to_account_idx].deposit(amount)
                print(f"{self.name} transferred ${amount} to {other_user.name}")
            else:
                print("Insufficient funds")
        else:
            print("Invalid account indices")


if __name__ == "__main__":
    user1 = User("Alice", "alice@example.com")
    user1.add_account().add_account(int_rate=0.05, balance=1000)

    user2 = User("Bob", "bob@example.com")
    user2.add_account(balance=500)

    user1.make_deposit(0, 500)
    user1.make_withdrawal(0, 200)
    user1.display_user_balance()

    user1.transfer_money(300, user2, 0, 0)

    user1.display_user_balance()
    user2.display_user_balance()