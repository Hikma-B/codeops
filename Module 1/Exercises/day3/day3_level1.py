# Lists & Tuples

# Create a list of 6 favorite foods
foods = ["Injera", "Pizza", "Burger", "Pasta", "Rice", "Chicken"]

# Print the first and last food
print("First food:", foods[0])
print("Last food:", foods[-1])

# Add a new food
foods.append("Salad")
print("After append:", foods)

# Remove the second food
foods.pop(1)
print("After pop:", foods)

# Create a tuple of coordinates for Ethiopia
coordinates = (9.1450, 40.4897)

# Unpack the tuple
latitude, longitude = coordinates

print("Latitude:", latitude)
print("Longitude:", longitude)

#Dictionaries

# Create a student dictionary
student = {
    "name": "Hikma",
    "age": 22,
    "grade": "A",
    "city": "Hawassa",
    "department": "Computer Science"
}

# Print the student's name, department, and grade
print("Name:", student["name"])
print("Department:", student["department"])
print("Grade:", student["grade"])

# Add a phone number
student["phone"] = "0987654321"

# Update the grade
student["grade"] = "A+"

# Print the updated dictionary
print(student)

#Sets

# Create a list with duplicate names
names = ["Hikma", "Ahmed", "Sara", "Hikma", "Ahmed", "Ali"]

# Convert the list to a set to remove duplicates
unique_names = set(names)

# Print the set
print("Unique names:", unique_names)

# Add a new name to the set
unique_names.add("Fatuma")

# Print the updated set
print("Updated set:", unique_names)