# Person Class

class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def introduce(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years old.")


# Create objects
person1 = Person("Hikma", 22)
person2 = Person("Ali", 25)

# Call the method
person1.introduce()
person2.introduce()

#Rectangle Class

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Create rectangle objects
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(7, 3)

# Display results
print("Rectangle 1")
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())

print("\nRectangle 2")
print("Area:", rectangle2.area())
print("Perimeter:", rectangle2.perimeter())

# Exercise 3: Bank Account (Basic)

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
        print(f"New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
            print(f"New Balance: {self.balance}")
        else:
            print("Insufficient balance!")


# Create an account object
account = Account("Hikma", 1000)

# Test deposit and withdrawal
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)


