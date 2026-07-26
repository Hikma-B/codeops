#List Operations

# Create a list of numbers
numbers = [10, 25, 40, 15, 60, 30]

# Print numbers greater than 30
print("Numbers greater than 30:")
for num in numbers:
    if num > 30:
        print(num)

# Sort the list
numbers.sort()
print("Sorted list:", numbers)

# Find the sum and average
total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

# Dictionary Operations

# Create a dictionary of products and prices
products = {
    "Laptop": 50000,
    "Phone": 20000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Headphones": 2500
}

# Print each product and its price
print("\nProduct List:")
for product, price in products.items():
    print(f"{product}: {price}")

# Ask the user for a product name
product_name = input("Enter a product name: ")

# Display the price or a default message
print(products.get(product_name, "Product not found"))

# Question 6: List Comprehension

# List of numbers from 1 to 20
numbers = [x for x in range(1, 21)]
print("Numbers from 1 to 20:")
print(numbers)

# Even numbers from 1 to 30
even_numbers = [x for x in range(1, 31) if x % 2 == 0]
print("Even numbers:")
print(even_numbers)

# Odd numbers from 1 to 10
odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
print("Odd numbers:")
print(odd_numbers)