# Intermediate Exercises

from abc import ABC, abstractmethod


# ----------------------------
# SRP + DIP
# ----------------------------

class NotificationService:
    def notify(self, message):
        print("Notification:", message)


class DatabaseService:
    def save(self, account):
        print(f"Account {account.number} saved to database.")


class Account:
    def __init__(self, owner, number, balance, notifier, database):
        self.owner = owner
        self.number = number
        self.balance = balance
        self.notifier = notifier
        self.database = database

    def deposit(self, amount):
        self.balance += amount
        self.database.save(self)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.database.save(self)
            self.notifier.notify("Withdrawal successful")
        else:
            print("Insufficient balance")

    def statement(self):
        print(f"\nOwner: {self.owner}")
        print(f"Account: {self.number}")
        print(f"Balance: {self.balance}")


# ----------------------------
# Factory Pattern
# ----------------------------

class SavingsAccount(Account):
    pass


class CurrentAccount(Account):
    pass


class FixedDepositAccount(Account):
    pass


class AccountFactory:
    @staticmethod
    def create(kind, owner, number, balance, notifier, database):
        if kind.lower() == "savings":
            return SavingsAccount(owner, number, balance, notifier, database)
        elif kind.lower() == "current":
            return CurrentAccount(owner, number, balance, notifier, database)
        elif kind.lower() == "fixed":
            return FixedDepositAccount(owner, number, balance, notifier, database)
        else:
            raise ValueError("Invalid account type")


# ----------------------------
# Observer Pattern
# ----------------------------

class SMSAlert:
    def update(self, amount):
        print(f"SMS Alert: Large withdrawal of {amount}")


class AuditLog:
    def update(self, amount):
        print(f"Audit Log: Withdrawal of {amount} recorded")


class ObservableAccount(Account):
    def __init__(self, owner, number, balance, notifier, database):
        super().__init__(owner, number, balance, notifier, database)
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, amount):
        for observer in self.observers:
            observer.update(amount)

    def withdraw(self, amount):
        super().withdraw(amount)
        if amount > 3000:
            self.notify_observers(amount)


# ----------------------------
# Interface Segregation Principle
# ----------------------------

class InterestBearing(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsInterestAccount(SavingsAccount, InterestBearing):
    def calculate_interest(self):
        return self.balance * 0.05


# ----------------------------
# Testing
# ----------------------------

notifier = NotificationService()
database = DatabaseService()

acc = AccountFactory.create(
    "savings",
    "Hikma",
    "1001",
    5000,
    notifier,
    database
)

acc.deposit(1000)
acc.statement()

obs = ObservableAccount(
    "Ali",
    "1002",
    6000,
    notifier,
    database
)

obs.add_observer(SMSAlert())
obs.add_observer(AuditLog())

obs.withdraw(3500)

interest_acc = SavingsInterestAccount(
    "Sara",
    "1003",
    10000,
    notifier,
    database
)

print("Interest:", interest_acc.calculate_interest())