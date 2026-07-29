# Day 7 - Advanced Exercises

import time
from collections import deque

# 9. Performance Comparison

numbers = list(range(10000))
dictionary = {i: i for i in range(10000)}

start = time.time()
9999 in numbers
print("List Search Time:", time.time() - start)

start = time.time()
9999 in dictionary
print("Dictionary Search Time:", time.time() - start)

# Insert at beginning of list
lst = []
start = time.time()
for i in range(10000):
    lst.insert(0, i)
print("List Insert Time:", time.time() - start)

# Insert using deque
dq = deque()
start = time.time()
for i in range(10000):
    dq.appendleft(i)
print("Deque Insert Time:", time.time() - start)

# 10. Choose the Right Structure

print("\nRecommended Data Structures")
print("Username lookup -> Dictionary/Set (O(1))")
print("Customer support queue -> Queue (FIFO)")
print("Undo feature -> Stack (LIFO)")
print("Student ID lookup -> Dictionary (O(1))")

# 11. Linked List vs Array

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def remove_middle(self):
        if self.head is None or self.head.next is None:
            return

        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Python List
items = [10, 20, 30, 40, 50]
items.pop(len(items) // 2)
print("\nPython List:", items)

# Linked List
ll = LinkedList()

for value in [10, 20, 30, 40, 50]:
    ll.append(value)

ll.remove_middle()
print("Linked List:")
ll.print_list()

print("\nTrade-off:")
print("Python list: Fast access, slow insert/delete in middle.")
print("Linked list: Slow access, fast insert/delete after finding node.")