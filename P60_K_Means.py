# File: main.py
# Author: Armstrong Subero
# Platform: MicroPython (Raspberry Pi Pico or similar)
# Program: P60_K_Means
# Interpreter: MicroPython
# Program Version: 1.2
#
# Program Description: This program demonstrates the implementation of the K-Means clustering
#                      algorithm on a 2D dataset. The algorithm partitions the data into K clusters
#                      by iteratively assigning data points to the nearest centroid and updating the centroids.

import random
import math

class KMeans:
    def __init__(self, k, max_iters=100):
        """
        Initialize the KMeans clustering algorithm.

        :param k: The number of clusters.
        :param max_iters: The maximum number of iterations to run the algorithm.
        """
        self.k = k
        self.max_iters = max_iters
        self.centroids = []

    def initialize_centroids(self, data):
        """
        Randomly initialize the centroids from the data points.

        :param data: List of data points [(x1, y1), (x2, y2), ...]
        """
        self.centroids = []
        selected_indices = []
        while len(self.centroids) < self.k:
            index = random.randint(0, len(data) - 1)
            if index not in selected_indices:
                self.centroids.append(data[index])
                selected_indices.append(index)

    def assign_clusters(self, data):
        """
        Assign each data point to the nearest centroid.

        :param data: List of data points [(x1, y1), (x2, y2), ...]
        :return: A list of cluster assignments for each data point.
        """
        clusters = []
        for point in data:
            distances = [self.euclidean_distance(point, centroid) for centroid in self.centroids]
            closest_centroid_index = distances.index(min(distances))
            clusters.append(closest_centroid_index)
        return clusters

    def update_centroids(self, data, clusters):
        """
        Update the centroids by calculating the mean of the points in each cluster.

        :param data: List of data points [(x1, y1), (x2, y2), ...]
        :param clusters: List of cluster assignments for each data point.
        """
        new_centroids = []
        for i in range(self.k):
            cluster_points = [data[j] for j in range(len(data)) if clusters[j] == i]
            if cluster_points:
                new_centroid = [sum(dim) / len(cluster_points) for dim in zip(*cluster_points)]
                new_centroids.append(new_centroid)
            else:
                new_centroids.append(self.centroids[i])  # Keep the old centroid if no points are assigned
        self.centroids = new_centroids

    def euclidean_distance(self, point1, point2):
        """
        Calculate the Euclidean distance between two points.

        :param point1: Tuple (x1, y1) representing the first point.
        :param point2: Tuple (x2, y2) representing the second point.
        :return: The Euclidean distance between the two points.
        """
        return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))

    def fit(self, data):
        """
        Fit the KMeans model to the data.

        :param data: List of data points [(x1, y1), (x2, y2), ...]
        :return: A tuple containing the final centroids and cluster assignments.
        """
        self.initialize_centroids(data)

        for _ in range(self.max_iters):
            clusters = self.assign_clusters(data)
            old_centroids = self.centroids[:]
            self.update_centroids(data, clusters)

            # Check for convergence (if centroids do not change)
            if old_centroids == self.centroids:
                break

        return self.centroids, clusters

# Example usage:
data = [
    [1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0],
    [1.0, 0.6], [9.0, 11.0], [8.0, 2.0], [10.0, 2.0],
    [9.0, 3.0]
]

# Initialize KMeans with 3 clusters
kmeans = KMeans(k=3)
centroids, clusters = kmeans.fit(data)

# Output the results
print("Final Centroids:", centroids)
print("Cluster Assignments:", clusters)
