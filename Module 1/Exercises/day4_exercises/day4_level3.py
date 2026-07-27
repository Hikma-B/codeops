#Full Bank Account with Properties

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}")

    def transfer(self, to_account, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            to_account.deposit(amount)
            print(f"Transferred {amount} to {to_account.owner}")
        else:
            print("Transfer failed. Insufficient balance.")


# Test the class
account1 = BankAccount("Hikma", 2000)
account2 = BankAccount("Ali", 1000)

account1.deposit(500)
account1.withdraw(300)
account1.transfer(account2, 700)

print("Hikma's Balance:", account1.balance)
print("Ali's Balance:", account2.balance)

#Library System

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} added to the library.")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                print(f"You borrowed '{book.title}'.")
                return
        print("Book is not available.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.available = True
                print(f"You returned '{book.title}'.")
                return
        print("Book not found.")


# Test the Library
library = Library()

book1 = Book("Python Basics", "John", "101")

library.add_book(book1)
library.borrow_book("101")
library.return_book("101")

#Car Class with Encapsulation

class Car:
    def __init__(self):
        self.__speed = 0
        self.__fuel = 50

    @property
    def speed(self):
        return self.__speed

    @property
    def fuel(self):
        return self.__fuel

    def accelerate(self):
        if self.__fuel > 0:
            self.__speed += 10
            self.__fuel -= 5
            print("Car accelerated.")
        else:
            print("No fuel!")

    def brake(self):
        if self.__speed >= 10:
            self.__speed -= 10
        print("Car slowed down.")

    def refuel(self, amount):
        self.__fuel += amount
        print(f"Added {amount} liters of fuel.")


# Test the Car class
car = Car()

car.accelerate()
car.accelerate()
car.brake()
car.refuel(20)

print("Speed:", car.speed)
print("Fuel:", car.fuel)