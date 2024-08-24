# File: main.py
# Author: Armstrong Subero
# Platform: MicroPython (Raspberry Pi Pico or similar)
# Program: P52_MicroPythonDecisionTree
# Interpreter: MicroPython
# Program Version: 1.0
#
# Program Description: This program demonstrates a basic implementation of a decision tree
#                      for binary classification in MicroPython. It includes the construction
#                      of the tree and prediction based on the tree.

class Node:
    def __init__(self, index=None, value=None, left=None, right=None, result=None):
        self.index = index    # Index of the feature used for splitting
        self.value = value    # Value of the feature used for splitting
        self.left = left      # Left subtree (for values < value)
        self.right = right    # Right subtree (for values >= value)
        self.result = result  # Result if the node is a leaf (classification label)

class DecisionTree:
    def __init__(self, max_depth=3):
        self.max_depth = max_depth
        self.root = None

    def fit(self, X, y):
        dataset = [X[i] + [y[i]] for i in range(len(X))]
        self.root = self._build_tree(dataset, 0)

    def _gini_impurity(self, groups, classes):
        n_instances = sum([len(group) for group in groups])
        gini = 0.0
        for group in groups:
            size = len(group)
            if size == 0:
                continue
            score = 0.0
            for class_val in classes:
                p = [row[-1] for row in group].count(class_val) / size
                score += p * p
            gini += (1.0 - score) * (size / n_instances)
        return gini

    def _test_split(self, index, value, dataset):
        left, right = [], []
        for row in dataset:
            if row[index] < value:
                left.append(row)
            else:
                right.append(row)
        return left, right

    def _get_split(self, dataset):
        class_values = list(set(row[-1] for row in dataset))
        best_index, best_value, best_score, best_groups = None, None, float('inf'), None
        for index in range(len(dataset[0]) - 1):
            for row in dataset:
                groups = self._test_split(index, row[index], dataset)
                gini = self._gini_impurity(groups, class_values)
                if gini < best_score:
                    best_index, best_value, best_score, best_groups = index, row[index], gini, groups
        return best_index, best_value, best_groups

    def _build_tree(self, dataset, depth):
        index, value, groups = self._get_split(dataset)
        left, right = groups
        
        # If no more splitting is possible, create a leaf node
        if not left or not right:
            return Node(result=self._to_terminal(left + right))
        
        # If max depth reached, create leaf nodes
        if depth >= self.max_depth:
            return Node(left=self._to_terminal(left), right=self._to_terminal(right))
        
        # Create decision node and recursively build left and right subtrees
        node = Node(index=index, value=value)
        node.left = self._build_tree(left, depth + 1)
        node.right = self._build_tree(right, depth + 1)
        
        return node

    def _to_terminal(self, group):
        outcomes = [row[-1] for row in group]
        return max(set(outcomes), key=outcomes.count)

    def predict(self, row):
        return self._predict_single(row, self.root)

    def _predict_single(self, row, node):
        if node.result is not None:
            return node.result
        if row[node.index] < node.value:
            return self._predict_single(row, node.left)
        else:
            return self._predict_single(row, node.right)

# Example usage:

X = [
    [2.771244718, 1.784783929],
    [1.728571309, 1.169761413],
    [3.678319846, 2.81281357],
    [3.961043357, 2.61995032],
    [2.999208922, 2.209014212],
    [7.497545867, 3.162953546],
    [9.00220326, 3.339047188],
    [7.444542326, 0.476683375],
    [10.12493903, 3.234550982],
    [6.642287351, 3.319983761]
]

y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# Initialize and train the decision tree
tree = DecisionTree(max_depth=3)
tree.fit(X, y)

# Make predictions
predictions = [tree.predict(row) for row in X]
print("Predictions:", predictions)
