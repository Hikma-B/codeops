# day5_level2.py

class Account:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance")

    def statement(self):
        print("\n----- Account Statement -----")
        print(f"Account Number: {self.account_number}")
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance, interest_rate):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest Added: {interest}")

    def statement(self):
        super().statement()
        print(f"Interest Rate: {self.interest_rate}%")


class CurrentAccount(Account):
    def __init__(self, account_number, owner, balance, overdraft_limit):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Overdraft limit exceeded!")

    def statement(self):
        super().statement()
        print(f"Overdraft Limit: {self.overdraft_limit}")


# ---------- Testing ----------

print("=== Savings Account ===")
saving = SavingsAccount("1001", "Hikma", 5000, 5)
saving.statement()
saving.deposit(1000)
saving.add_interest()
saving.statement()

print("\n=== Current Account ===")
current = CurrentAccount("2001", "Ali", 3000, 2000)
current.statement()
current.withdraw(4500)
current.statement()

print("\n=== Polymorphism ===")
accounts = [
    Account("3001", "Ahmed", 1000),
    SavingsAccount("3002", "Sara", 2000, 4),
    CurrentAccount("3003", "John", 1500, 1000)
]

for account in accounts:
    account.statement()
    account.deposit(100)