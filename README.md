# Modified K-Means Clustering (Using Manhattan Distance)

This is a simple Python project where I modified the classic K-Means clustering algorithm.
Instead of the normal Euclidean distance, this version uses Manhattan distance to calculate how close points are to the cluster centers.

Also, instead of using a fancy plotting library, the final result is shown as a 2D grid printed directly to the console using just print().

# What This Project Does

. Randomly generates 100 points and 10 cluster centers inside a 20×20 grid.

. Clusters the points using Manhattan distance (the sum of x and y differences).

. Updates cluster centers based on the average position of points in that cluster.

. Prints a simple 2D view of points (P) and cluster centers (C) in the console.

# Why Manhattan Distance?

Instead of using the straight-line distance (like with Euclidean), Manhattan distance measures how far you would travel in a grid, like streets on a city map.
It’s simple and can lead to interesting cluster shapes!

# Simple Output : 
![image](https://github.com/user-attachments/assets/b19cdc23-d4a8-4abe-8260-e91963b1da31)
