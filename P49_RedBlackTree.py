# File: main.py
# Author: Armstrong Subero
# Platform: Python (Standard or MicroPython)
# Program: P49_RedBlackTree
# Interpreter: Python 3.x
# Program Version: 1.0
#
# Program Description: This program demonstrates the creation of a Red-Black Tree
#                      with insertion functionality and maintaining the Red-Black properties.
#
# Notes:
# A Red-Black Tree is a balanced binary search tree with an extra bit of storage per node: its color, which can be red or black.

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 'red'  # New nodes are always red

class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 'black'
        self.root = self.TNULL

    def insert(self, key):
        node = Node(key)
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 'red'

        parent = None
        current = self.root

        while current != self.TNULL:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

        if node.parent is None:
            node.color = 'black'
            return

        if node.parent.parent is None:
            return

        self._fix_insert(node)

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def _fix_insert(self, k):
        while k.parent.color == 'red':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._rotate_right(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self._rotate_left(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._rotate_left(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self._rotate_right(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black'

    def inorder(self):
        self._inorder_helper(self.root)

    def _inorder_helper(self, node):
        if node != self.TNULL:
            self._inorder_helper(node.left)
            print(node.data, end=" ")
            self._inorder_helper(node.right)

# Example usage:

rbt = RedBlackTree()

# Insert some elements
rbt.insert(20)
rbt.insert(15)
rbt.insert(25)
rbt.insert(10)
rbt.insert(5)
rbt.insert(1)

# Perform an inorder traversal
print("Inorder Traversal of Red-Black Tree:")
rbt.inorder()  # Output: 1 5 10 15 20 25
