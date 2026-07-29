# Reverse a string using recursion
def reverse_string(text):
    if text == "":
        return ""
    return reverse_string(text[1:]) + text[0]

print("Reverse:", reverse_string("Python"))


# Count occurrences using recursion
def count_occurrences(lst, target):
    if len(lst) == 0:
        return 0
    if lst[0] == target:
        return 1 + count_occurrences(lst[1:], target)
    return count_occurrences(lst[1:], target)

numbers = [1, 2, 3, 2, 4, 2]
print("Occurrences of 2:", count_occurrences(numbers, 2))

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([64, 25, 12, 22, 11]))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort([64, 25, 12, 22, 11]))

def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            return arr[left], arr[right]
        elif current < target:
            left += 1
        else:
            right -= 1

    return None

numbers = [1, 2, 3, 4, 6, 8, 10]
print(two_sum(numbers, 10))