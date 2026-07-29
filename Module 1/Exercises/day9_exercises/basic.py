# Tree Basics

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def print_tree(node, level=0):
    print("  " * level + node.name)
    for child in node.children:
        print_tree(child, level + 1)

head = TreeNode("Head Office")
bole = TreeNode("Bole Branch")
piassa = TreeNode("Piassa Branch")
teller = TreeNode("Teller")
loan = TreeNode("Loan Officer")

head.add_child(bole)
head.add_child(piassa)
bole.add_child(teller)
bole.add_child(loan)

print_tree(head)