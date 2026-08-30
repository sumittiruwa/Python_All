"""DSA Practice: Kruskal's Minimum Spanning Tree Algorithm"""


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            return True
        return False


def kruskal_mst(num_vertices, edges):
    edges = sorted(edges, key=lambda edge: edge[2])
    ds = DisjointSet(num_vertices)
    mst = []

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))

    return mst


if __name__ == "__main__":
    edges = [
        (0, 1, 4), (0, 2, 4), (1, 2, 2),
        (2, 3, 3), (2, 5, 2), (2, 4, 4),
        (3, 4, 3), (5, 4, 3),
    ]

    mst = kruskal_mst(6, edges)
    print("Minimum Spanning Tree edges:", mst)
    print("Total weight:", sum(weight for _, _, weight in mst))
