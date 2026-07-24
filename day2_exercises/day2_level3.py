# Day 2 - Level 3
# Exercise 9: Tip Calculator

def calculate_tip(bill, tip_percent):
    return bill * tip_percent / 100

def calculate_total(bill, tip):
    return bill + tip

# Get input from the user
bill = float(input("Enter the bill amount: "))
tip_percent = int(input("Enter tip percentage (10, 15, or 20): "))
people = int(input("Enter number of people splitting the bill: "))

# Calculate values
tip = calculate_tip(bill, tip_percent)
total = calculate_total(bill, tip)
each_person = total / people

# Display results
print(f"\nTip amount: {tip:.2f}")
print(f"Total amount: {total:.2f}")
print(f"Each person pays: {each_person:.2f}")

# Exercise 10: Simple Quiz Game

def quiz():
    score = 0

    print("\nWelcome to the Quiz!")

    if input("1. What is the capital of Ethiopia? ") == "Addis Ababa":
        score += 1

    if input("2. How many days are there in a week? ") == "7":
        score += 1

    if input("3. What is 5 + 5? ") == "10":
        score += 1

    if input("4. What color is the sky on a clear day? ").lower() == "blue":
        score += 1

    if input("5. Which programming language are you learning? ").lower() == "python":
        score += 1

    print(f"\nYour final score is: {score}/5")

    if score == 5:
        print("Excellent!")
    elif score >= 3:
        print("Good job!")
    else:
        print("Keep practicing!")
quiz()

# Function with Default & Return

def calculate_final_price(price, tax_rate=0.15, discount=0):
    tax = price * tax_rate
    final_price = price + tax - discount
    return final_price

# Test the function
print("\nFinal Price 1:", calculate_final_price(100))
print("Final Price 2:", calculate_final_price(200, 0.15, 20))
print("Final Price 3:", calculate_final_price(500, 0.10, 50))