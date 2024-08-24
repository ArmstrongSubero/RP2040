# File: main.py
# Author: Armstrong Subero
# Platform: Python (Standard or MicroPython)
# Program: P50_Trie
# Interpreter: Python 3.x / MicroPython
# Program Version: 1.0
#
# Program Description: This program demonstrates the creation of a Trie (Prefix Tree)
#                      and implements basic operations like insertion, search, and prefix matching.
#
# Notes:
# A Trie is a special type of tree used to store strings, where each node represents a single character.
# Tries are commonly used for autocomplete systems, spell checkers, and IP routing.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True
        print(f"Inserted '{word}' into the trie.")

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True

# Example usage:

trie = Trie()

# Insert words into the trie
trie.insert("apple")
trie.insert("app")
trie.insert("apex")
trie.insert("bat")
trie.insert("ball")

# Search for words in the trie
print("Search for 'apple':", trie.search("apple"))  # Output: True
print("Search for 'app':", trie.search("app"))      # Output: True
print("Search for 'apex':", trie.search("apex"))    # Output: True
print("Search for 'bat':", trie.search("bat"))      # Output: True
print("Search for 'ball':", trie.search("ball"))    # Output: True
print("Search for 'balm':", trie.search("balm"))    # Output: False

# Check if any word starts with a given prefix
print("Starts with 'app':", trie.starts_with("app"))  # Output: True
print("Starts with 'bat':", trie.starts_with("bat"))  # Output: True
print("Starts with 'ba':", trie.starts_with("ba"))    # Output: True
print("Starts with 'ca':", trie.starts_with("ca"))    # Output: False
