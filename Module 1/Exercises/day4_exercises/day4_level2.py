# Exercise 4: Student Class

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


# Create a student object
student = Student("Hikma", "CS001")

# Add grades
student.add_grade(80)
student.add_grade(90)
student.add_grade(85)

# Display result
print("Student Name:", student.name)
print("Student ID:", student.student_id)
print("Average Grade:", student.average_grade())


#Product Class

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            print(f"Sold {quantity} {self.name}(s)")
            print(f"Remaining stock: {self.stock}")
        else:
            print("Not enough stock!")

    def restock(self, quantity):
        self.stock += quantity
        print(f"Added {quantity} items")
        print(f"Current stock: {self.stock}")


# Create a product object
product = Product("Laptop", 50000, 10)

# Test the methods
product.sell(3)
product.restock(5)
product.sell(20)

#Encapsulation Practice

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrew: {amount}")


# Test the class
account = Account("Hikma", 1000)

print("Current Balance:", account.balance)

account.deposit(500)
print("Balance:", account.balance)

account.withdraw(300)
print("Balance:", account.balance)

account.withdraw(2000)