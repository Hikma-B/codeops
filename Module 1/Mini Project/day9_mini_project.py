import heapq
from collections import deque

# ---------------- TREE ----------------
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(TreeNode(child))

    def print_tree(self, level=0):
        print("  " * level + self.name)
        for child in self.children:
            child.print_tree(level + 1)

root = TreeNode("Head Office")
root.add_child("Bole Branch")
root.add_child("Piassa Branch")

# ---------------- GRAPH ----------------
graph = {
    "Almaz": ["Dawit"],
    "Dawit": ["Tigist"],
    "Tigist": ["Hanna"],
    "Hanna": []
}

def add_connection(a, b):
    if a not in graph:
        graph[a] = []
    graph[a].append(b)

def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph.get(node, []))
    print()

def dfs(start, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        print(start, end=" ")
        visited.add(start)

        for neighbor in graph.get(start, []):
            dfs(neighbor, visited)

# ---------------- BST ----------------
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return BSTNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

def search(root, value):
    if root is None:
        return False

    if root.value == value:
        return True

    if value < root.value:
        return search(root.left, value)

    return search(root.right, value)

bst = None
for account in [50, 30, 70, 20, 40, 60]:
    bst = insert(bst, account)

# ---------------- HEAP ----------------
heap = []

def add_transaction(priority, name):
    heapq.heappush(heap, (-priority, name))

def process_transaction():
    if heap:
        print("Processing:", heapq.heappop(heap))
    else:
        print("No urgent transactions.")

# ---------------- MENU ----------------
while True:
    print("\n===== Addis Bank Network System =====")
    print("1. Show Branch Hierarchy")
    print("2. Add Branch/Employee")
    print("3. Add Money Transfer Connection")
    print("4. Show Customers (BFS)")
    print("5. Show Customers (DFS)")
    print("6. Add Urgent Transaction")
    print("7. Process Highest Priority")
    print("8. Search Customer Account (BST)")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        root.print_tree()

    elif choice == "2":
        name = input("Enter branch/employee: ")
        root.add_child(name)

    elif choice == "3":
        a = input("From customer: ")
        b = input("To customer: ")
        add_connection(a, b)

    elif choice == "4":
        start = input("Start customer: ")
        bfs(start)

    elif choice == "5":
        start = input("Start customer: ")
        dfs(start)
        print()

    elif choice == "6":
        priority = int(input("Priority: "))
        name = input("Transaction: ")
        add_transaction(priority, name)

    elif choice == "7":
        process_transaction()

    elif choice == "8":
        account = int(input("Account number: "))
        if search(bst, account):
            print("Account Found")
        else:
            print("Account Not Found")

    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")