# Binary Search Tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None:
        return False
    if root.key == key:
        return True
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

root = None
for value in [50, 30, 70, 20, 40, 60]:
    root = insert(root, value)

print(search(root, 40))
print(search(root, 100))