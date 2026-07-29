# Bank Transaction Analyzer

transactions = [
    {"amount": 500, "date": "2026-07-20", "type": "Deposit"},
    {"amount": 200, "date": "2026-07-21", "type": "Withdraw"},
    {"amount": 1000, "date": "2026-07-22", "type": "Deposit"},
    {"amount": 300, "date": "2026-07-23", "type": "Withdraw"},
]

# Recursive total balance
def total_balance(transactions, index=0):
    if index == len(transactions):
        return 0

    amount = transactions[index]["amount"]
    if transactions[index]["type"] == "Withdraw":
        amount = -amount

    return amount + total_balance(transactions, index + 1)

# Sort by amount
def sort_by_amount(data):
    return sorted(data, key=lambda x: x["amount"])

# Linear search
def linear_search(data, amount):
    for t in data:
        if t["amount"] == amount:
            return t
    return None

# Binary search (after sorting)
def binary_search(data, target):
    left, right = 0, len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid]["amount"] == target:
            return data[mid]
        elif data[mid]["amount"] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

print("Total Balance:", total_balance(transactions))

sorted_transactions = sort_by_amount(transactions)

print("\nSorted Transactions:")
for t in sorted_transactions:
    print(t)

print("\nLinear Search:", linear_search(transactions, 1000))
print("Binary Search:", binary_search(sorted_transactions, 1000))