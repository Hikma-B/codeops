# Day 2 - Level 1
# Exercise 1: Variables and Data Types

full_name = "Hikma"
age = 22
height = 1.65
is_student = True
favorite_food = "Rice"

print(f"Hello! My name is {full_name}.")
print(f"I am {age} years old.")
print(f"My height is {height} meters.")
print(f"Am I a student? {is_student}")
print(f"My favorite food is {favorite_food}.")

# Arithmetic Operations

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"\nResults for {num1} and {num2}")
print(f"Sum = {num1 + num2}")
print(f"Difference = {num1 - num2}")
print(f"Product = {num1 * num2}")
print(f"Division = {num1 / num2}")
print(f"Floor Division = {num1 // num2}")
print(f"Remainder = {num1 % num2}")

# Exercise 3: Type Conversion

birth_year = int(input("\nEnter your birth year: "))
age = 2026 - birth_year

print(f"You are {age} years old.")

# Simple Decision

score = int(input("\nEnter your score (0-100): "))

if score >= 50:
    print("Pass")
else:
    print("Fail")