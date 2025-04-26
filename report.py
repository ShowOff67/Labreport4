import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None

class KMeans:
    def __init__(self, points, clusters):
        self.points = points
        self.clusters = clusters
        self.grid_size = 20
        self.mat = [[' . ' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.start()

    def start(self):
        # generate points and clusters randomly
        self.p = [Point(random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)) for _ in range(self.points)]
        self.k = [Point(random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)) for _ in range(self.clusters)]

        while True:
            # assign points to nearest cluster using Manhattan distance
            for i in range(self.points):
                min_dist = float('inf')
                for j in range(self.clusters):
                    d1 = abs(self.k[j].x - self.p[i].x) + abs(self.k[j].y - self.p[i].y)  # Manhattan distance
                    if d1 < min_dist:
                        self.p[i].cluster = j
                        min_dist = d1

            # backup
            kdup = [Point(self.k[i].x, self.k[i].y) for i in range(self.clusters)]

            for j in range(self.clusters):
                x, y, count = 0, 0, 0
                for i in range(self.points):
                    if self.p[i].cluster == j:
                        x += self.p[i].x
                        y += self.p[i].y
                        count += 1
                if count != 0:
                    self.k[j].x = round(x / count)
                    self.k[j].y = round(y / count)

            # check for convergence
            err = 0
            for i in range(self.clusters):
                err += abs(self.k[i].x - kdup[i].x) + abs(self.k[i].y - kdup[i].y)

            if err == 0:
                break

        # fill the matrix with points
        for p in self.p:
            self.mat[p.y][p.x] = ' P '

        # mark cluster centers
        for k in self.k:
            self.mat[k.y][k.x] = ' C '

        # print the matrix
        print("\nFinal Clustering Visualization:\n")
        for row in reversed(self.mat):  # Print from top (higher y) to bottom (lower y)
            print(''.join(row))

        # print cluster details
        for i, k in enumerate(self.k):
            print(f"Cluster {i + 1} center at ({k.x}, {k.y})")

def main():
    points = 100  # fixed number of points 100
    clusters = 10 # fixed number of clusters 10
    kmeans = KMeans(points, clusters)

if __name__ == "__main__":
    main()
