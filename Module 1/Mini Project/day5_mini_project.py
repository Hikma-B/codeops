from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    def statement(self):
        print("\n---------------------------")
        print(f"Account Number: {self.account_number}")
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")

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
        self.balance += self.calculate_interest()

    def statement(self):
        super().statement()
        print(f"Type: Savings")
        print(f"Interest Rate: {self.interest_rate}%")


class CurrentAccount(Account):
    def __init__(self, account_number, owner, balance, overdraft_limit):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Overdraft limit exceeded!")

    def calculate_interest(self):
        return 0

    def statement(self):
        super().statement()
        print("Type: Current")
        print(f"Overdraft Limit: {self.overdraft_limit}")


accounts = []

while True:
    print("\n===== Addis Bank System =====")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Show Statement")
    print("6. Apply Interest to Savings Accounts")
    print("7. Show All Accounts")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        acc = input("Account Number: ")
        owner = input("Owner Name: ")
        balance = float(input("Initial Balance: "))
        rate = float(input("Interest Rate (%): "))
        accounts.append(SavingsAccount(acc, owner, balance, rate))
        print("Savings account created.")

    elif choice == "2":
        acc = input("Account Number: ")
        owner = input("Owner Name: ")
        balance = float(input("Initial Balance: "))
        overdraft = float(input("Overdraft Limit: "))
        accounts.append(CurrentAccount(acc, owner, balance, overdraft))
        print("Current account created.")

    elif choice == "3":
        acc = input("Account Number: ")
        amount = float(input("Deposit Amount: "))
        for account in accounts:
            if account.account_number == acc:
                account.deposit(amount)
                break

    elif choice == "4":
        acc = input("Account Number: ")
        amount = float(input("Withdraw Amount: "))
        for account in accounts:
            if account.account_number == acc:
                account.withdraw(amount)
                break

    elif choice == "5":
        acc = input("Account Number: ")
        for account in accounts:
            if account.account_number == acc:
                account.statement()
                break

    elif choice == "6":
        for account in accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest()
        print("Interest applied to all savings accounts.")

    elif choice == "7":
        if not accounts:
            print("No accounts found.")
        else:
            for account in accounts:
                account.statement()

    elif choice == "8":
        print("Thank you for using Addis Bank System.")
        break

    else:
        print("Invalid choice. Try again.")