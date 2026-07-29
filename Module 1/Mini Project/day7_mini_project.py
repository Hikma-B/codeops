# Day 7 Mini Project
# Bank Customer Service Simulator

customers = {
    "1001": "Hikma",
    "1002": "Ali",
    "1003": "Sara"
}

transaction_history = []  # Stack

while True:
    print("\n===== Addis Bank Customer Service =====")
    print("1. Make Transaction")
    print("2. Undo Last Transaction")
    print("3. Search Customer")
    print("4. Show Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        acc = input("Enter Account Number: ")

        if acc in customers:
            transaction = input("Enter Transaction: ")
            transaction_history.append(transaction)  # O(1)
            print("Transaction saved.")
        else:
            print("Customer not found.")

    elif choice == "2":
        if transaction_history:
            last = transaction_history.pop()  # O(1)
            print("Undone:", last)
        else:
            print("No transaction to undo.")

    elif choice == "3":
        acc = input("Enter Account Number: ")

        if acc in customers:  # O(1)
            print("Customer:", customers[acc])
        else:
            print("Customer not found.")

    elif choice == "4":
        print("\nTransaction History:")
        if not transaction_history:
            print("No transactions.")
        else:
            for transaction in transaction_history:
                print(transaction)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")