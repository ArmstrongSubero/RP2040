# File: main.py
# Author: Armstrong Subero
# Platform: Python (Standard or MicroPython)
# Program: P48_BinarySearchTree
# Interpreter: Python 3.x / MicroPython
# Program Version: 1.0
#
# Program Description: This program demonstrates the creation of a binary search tree (BST)
#                      and implements basic operations like insertion and search.
#
# Notes:
# A binary search tree (BST) is a tree data structure in which each node has at most two children.
# For each node, all elements in the left subtree are less than the node, and all elements in the
# right subtree are greater.

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = BSTNode(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = BSTNode(value)
            else:
                self._insert(value, current_node.right)
        else:
            print("Value already in tree!")

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, current_node):
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left is not None:
            return self._search(value, current_node.left)
        elif value > current_node.value and current_node.right is not None:
            return self._search(value, current_node.right)
        return False

# Example usage:
# Constructing the following binary search tree:
#         8
#        / \
#       3   10
#      / \    \
#     1   6    14
#        / \   /
#       4   7 13

bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)
bst.insert(4)
bst.insert(7)
bst.insert(13)

# Search for elements
print("Search for 7:", bst.search(7))  # Output: True
print("Search for 2:", bst.search(2))  # Output: False
