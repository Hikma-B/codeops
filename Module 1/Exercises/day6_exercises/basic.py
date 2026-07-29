# Single Responsibility Principle (SRP)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class SalaryCalculator:
    def calculate_salary(self, employee):
        return employee.salary


class FileManager:
    def save_to_file(self, employee):
        print(f"{employee.name} saved to file.")


class EmailService:
    def send_email(self, employee):
        print(f"Email sent to {employee.name}")


# Open/Closed Principle (OCP)

class Bonus:
    def calculate_bonus(self):
        pass


class FullTimeEmployee(Bonus):
    def calculate_bonus(self):
        return 5000


class PartTimeEmployee(Bonus):
    def calculate_bonus(self):
        return 2000


# Liskov Substitution Principle (LSP)

class Bird:
    def move(self):
        print("Bird is moving")


class FlyingBird(Bird):
    def fly(self):
        print("Bird is flying")


class Penguin(Bird):
    def move(self):
        print("Penguin is walking")


def move_bird(bird):
    bird.move()


# Testing

employee = Employee("Hikma", 10000)

salary = SalaryCalculator()
print("Salary:", salary.calculate_salary(employee))

file = FileManager()
file.save_to_file(employee)

email = EmailService()
email.send_email(employee)

full = FullTimeEmployee()
part = PartTimeEmployee()

print("Full Time Bonus:", full.calculate_bonus())
print("Part Time Bonus:", part.calculate_bonus())

sparrow = FlyingBird()
penguin = Penguin()

move_bird(sparrow)
move_bird(penguin)

print("\nSOLID Violation:")
print("SRP violated because Account handles banking, email and database.")
print("DIP violated because Account depends directly on EmailNotifier.")