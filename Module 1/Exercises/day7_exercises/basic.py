# Day 7 - Basic Exercises

# 1. Big-O Notation
print("1. Big-O Notation")
print("Access list by index: O(1)")
print("Search in list: O(n)")
print("Insert at beginning of list: O(n)")
print("Dictionary lookup: O(1)")

# 2. Compare Complexities
print("\n2. Fastest to Slowest")
print("O(1) -> O(log n) -> O(n) -> O(n^2)")

# 3. Arrays / Lists
print("\n3. Lists")

students = [
    "Hikma", "Ali", "Sara", "Ahmed", "John",
    "Amina", "Abel", "Meron", "Kebede", "Helen"
]

print("First Student:", students[0])

students.append("Marta")
print("After Append:", students)

students.insert(0, "Daniel")
print("After Insert:", students)

# 4. Dictionaries
print("\n4. Dictionary")

student_grades = {
    "Hikma": 90,
    "Ali": 85,
    "Sara": 95,
    "Ahmed": 80,
    "John": 88
}

student_grades["Marta"] = 91
student_grades["Ali"] = 89

print(student_grades)

name = "Sara"

if name in student_grades:
    print(name, "exists.")
else:
    print(name, "not found.")