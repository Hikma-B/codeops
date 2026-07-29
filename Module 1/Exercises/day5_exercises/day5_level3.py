from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_number, owner, balance):
        self._account_number = account_number
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance")

    def statement(self):
        print("\n----- Account Statement -----")
        print(f"Account Number: {self._account_number}")
        print(f"Owner: {self._owner}")
        print(f"Balance: {self._balance}")

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance, interest_rate):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100

    def add_interest(self):
        interest = self.calculate_interest()
        self._balance += interest
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
            self._balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Overdraft limit exceeded!")

    def calculate_interest(self):
        return 0

    def statement(self):
        super().statement()
        print(f"Overdraft Limit: {self.overdraft_limit}")


# ---------- Testing ----------

saving = SavingsAccount("1001", "Hikma", 5000, 5)
current = CurrentAccount("2001", "Ali", 3000, 2000)

accounts = [saving, current]

for account in accounts:
    account.statement()
    account.deposit(100)

saving.add_interest()

print("\nInterest on Savings:", saving.calculate_interest())
print("Interest on Current:", current.calculate_interest())