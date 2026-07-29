# Day 7 - Intermediate Exercises

# 5. Big-O Analysis

def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


numbers = [5, 2, 9, 1, 7, 10]
print("Maximum:", find_max(numbers))
print("Time Complexity: O(n)")


def nested_loops(n):
    for i in range(n):
        for j in range(n):
            pass

print("Nested Loops Time Complexity: O(n^2)")


# 6. Linked List

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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

print("\nLinked List:")
ll.print_list()


# 7. Stack (LIFO)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]


stack = Stack()

text = "Addis Ababa"

for ch in text:
    stack.push(ch)

reversed_text = ""

while stack.items:
    reversed_text += stack.pop()

print("\nReversed String:", reversed_text)


# 8. Queue (FIFO)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)


queue = Queue()

queue.enqueue("Customer 1")
queue.enqueue("Customer 2")
queue.enqueue("Customer 3")

print("\nServing Customers:")
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())