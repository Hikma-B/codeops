#Factorial (Recursive)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Recursive:", factorial(5))


# Iterative version
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Iterative:", factorial_iterative(5))

#  Recursive Sum of a List

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])

nums = [10, 20, 30, 40, 50]
print("Sum:", sum_list(nums))

#Linear Search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [5, 10, 15, 20, 25]

print("Index of 15:", linear_search(numbers, 15))
print("Index of 30:", linear_search(numbers, 30))

