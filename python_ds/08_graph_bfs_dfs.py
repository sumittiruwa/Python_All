"""
DSA Practice: Graph Traversal
Implements BFS and DFS on a graph represented as an adjacency list.
"""

from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        self.adjacency_list.setdefault(u, []).append(v)
        self.adjacency_list.setdefault(v, []).append(u)

    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adjacency_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start):
        visited = set()
        order = []
        self._dfs(start, visited, order)
        return order

    def _dfs(self, node, visited, order):
        visited.add(node)
        order.append(node)
        for neighbor in self.adjacency_list.get(node, []):
            if neighbor not in visited:
                self._dfs(neighbor, visited, order)


if __name__ == "__main__":
    g = Graph()
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
    for u, v in edges:
        g.add_edge(u, v)

    print("BFS from 1:", g.bfs(1))
    print("DFS from 1:", g.dfs(1))
