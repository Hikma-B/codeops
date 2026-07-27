#Bank Account System

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance!")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.__balance}")

        # Test the program

account = BankAccount("Hikma", 1000)

account.show_balance()
account.deposit(500)
account.withdraw(300)
account.show_balance()
account.withdraw(2000)