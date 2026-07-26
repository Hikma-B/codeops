# Inventory Manager

inventory = {}

while True:
    print("\n===== Inventory Manager =====")
    print("1. Add new product")
    print("2. Update quantity")
    print("3. View all products")
    print("4. Save to file")
    print("5. Load from file")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        inventory[product] = quantity
        print("Product added.")

    elif choice == "2":
        product = input("Enter product name: ")
        if product in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[product] = quantity
            print("Quantity updated.")
        else:
            print("Product not found.")

    elif choice == "3":
        print("\nInventory:")
        if inventory:
            for product, quantity in inventory.items():
                print(f"{product}: {quantity}")
        else:
            print("Inventory is empty.")

    elif choice == "4":
        with open("inventory.txt", "w") as file:
            for product, quantity in inventory.items():
                file.write(f"{product},{quantity}\n")
        print("Inventory saved.")

    elif choice == "5":
        try:
            with open("inventory.txt", "r") as file:
                inventory.clear()
                for line in file:
                    product, quantity = line.strip().split(",")
                    inventory[product] = int(quantity)
            print("Inventory loaded.")
        except FileNotFoundError:
            print("No inventory file found.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")