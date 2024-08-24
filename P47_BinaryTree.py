# File: main.py
# Author: Armstrong Subero
# Platform: Python (Standard or MicroPython)
# Program: P47_BinaryTree
# Interpreter: Python 3.x / MicroPython
# Program Version: 1.0
#
# Program Description: This program demonstrates the creation of a binary tree
#                      and implements basic tree traversal methods: Inorder, Preorder, and Postorder.
#
# Notes:
# A binary tree is a tree data structure where each node has at most two children,
# referred to as the left child and the right child. Can be used in task scheduling

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    # Inorder Traversal (Left, Root, Right)
    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + " ")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    # Preorder Traversal (Root, Left, Right)
    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + " ")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    # Postorder Traversal (Left, Right, Root)
    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + " ")
        return traversal

# Example usage:
# Constructing the following binary tree:
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

binary_tree = BinaryTree(1)
binary_tree.root.left = Node(2)
binary_tree.root.right = Node(3)
binary_tree.root.left.left = Node(4)
binary_tree.root.left.right = Node(5)
binary_tree.root.right.right = Node(6)

# Inorder Traversal
print("Inorder Traversal:", binary_tree.inorder_traversal(binary_tree.root, ""))  # Output: 4 2 5 1 3 6

# Preorder Traversal
print("Preorder Traversal:", binary_tree.preorder_traversal(binary_tree.root, ""))  # Output: 1 2 4 5 3 6

# Postorder Traversal
print("Postorder Traversal:", binary_tree.postorder_traversal(binary_tree.root, ""))  # Output: 4 5 2 6 3 1
