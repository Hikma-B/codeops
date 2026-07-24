# Day 2 - Level 2
# Exercise 5: Grade Classifier

score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Excellent")
elif 80 <= score <= 89:
    print("Very Good")
elif 70 <= score <= 79:
    print("Good")
elif 50 <= score <= 69:
    print("Pass")
else:
    print("Fail")

    # Number Pattern

print("\nNumbers from 1 to 20:")
for number in range(1, 21):
    print(number)

print("\nOdd numbers:")
for number in range(1, 21):
    if number % 2 != 0:
        print(number)

print("\nNumbers divisible by 5:")
for number in range(1, 21):
    if number % 5 == 0:
        print(number)

        #While Loop Practice

total = 0

while True:
    number = int(input("Enter a positive number (0 to stop): "))

    if number == 0:
        break

    total += number

print(f"The total sum is: {total}")

#Function Practice

# Function 1
def greet(name):
    print(f"Welcome, {name}!")

# Function 2
def square(number):
    return number * number

# Function 3
def is_even(number):
    return number % 2 == 0

# Testing the functions
greet("Hikma")

print("Square of 5 is:", square(5))

print("Is 8 even?", is_even(8))
print("Is 7 even?", is_even(7))

