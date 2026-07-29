from abc import ABC, abstractmethod


# Singleton Pattern
class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 5
        return cls._instance


# Observer Pattern
class SMSAlert:
    def update(self, message):
        print("SMS Alert:", message)


class AuditLog:
    def update(self, message):
        print("Audit Log:", message)


# Abstract Account Class
class Account(ABC):
    def __init__(self, owner, number, balance):
        self.owner = owner
        self.number = number
        self.balance = balance
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass

    def statement(self):
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.number}")
        print(f"Balance: {self.balance}")


class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            if amount > 3000:
                self.notify(f"Large withdrawal: {amount}")
        else:
            print("Insufficient balance")


class CurrentAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            if amount > 3000:
                self.notify(f"Large withdrawal: {amount}")
        else:
            print("Insufficient balance")


class InvestmentAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            if amount > 3000:
                self.notify(f"Large withdrawal: {amount}")
        else:
            print("Insufficient balance")


# Factory Pattern
class AccountFactory:
    @staticmethod
    def create(kind, owner, number, balance):
        if kind == "savings":
            return SavingsAccount(owner, number, balance)
        elif kind == "current":
            return CurrentAccount(owner, number, balance)
        elif kind == "investment":
            return InvestmentAccount(owner, number, balance)
        else:
            raise ValueError("Invalid account type")


# Testing
config = BankConfig()
print("Interest Rate:", config.interest_rate)

account = AccountFactory.create("savings", "Hikma", "1001", 5000)

account.add_observer(SMSAlert())
account.add_observer(AuditLog())

account.withdraw(3500)
account.statement()