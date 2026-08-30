"""DSA Practice: Disjoint Set (Union-Find) with path compression and union by rank"""


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    ds = DisjointSet(6)
    ds.union(0, 1)
    ds.union(1, 2)
    ds.union(3, 4)

    print("0 and 2 connected:", ds.connected(0, 2))
    print("0 and 3 connected:", ds.connected(0, 3))

    ds.union(2, 3)
    print("0 and 3 connected after union:", ds.connected(0, 3))
