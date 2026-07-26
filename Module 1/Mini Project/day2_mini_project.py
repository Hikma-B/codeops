# Day 2 Mini Project: Personal Finance Tracker

balance = 0

def add_income():
    global balance
    amount = float(input("Enter income: "))
    balance += amount
    print("Income added successfully!")

def add_expense():
    global balance
    amount = float(input("Enter expense: "))
    balance -= amount
    print("Expense added successfully!")

def show_balance():
    print(f"Current Balance: {balance}")

while True:
    print("\n===== Personal Finance Tracker =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Exit")

    try:
        choice = int(input("Choose an option: "))

        if choice == 1:
            add_income()
        elif choice == 2:
            add_expense()
        elif choice == 3:
            show_balance()
        elif choice == 4:
            print("Final Balance:", balance)
            print("Thank you for using the Personal Finance Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Please enter a valid number.")