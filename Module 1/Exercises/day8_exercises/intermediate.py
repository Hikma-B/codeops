#Binary Search

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

numbers = [5, 10, 15, 20, 25]

print("Index of 20:", binary_search(numbers, 20))
print("Index of 7:", binary_search(numbers, 7))

#Bubble Sort

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        print(f"Pass {i + 1}: {arr}")

numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original:", numbers)
bubble_sort(numbers)
print("Sorted:", numbers)