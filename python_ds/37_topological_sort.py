"""DSA Practice: Topological Sort on a Directed Acyclic Graph (DFS-based)"""


def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]


if __name__ == "__main__":
    graph = {
        "shirt": ["jacket"],
        "tie": ["jacket"],
        "jacket": [],
        "pants": ["shoes", "belt"],
        "belt": ["jacket"],
        "shoes": [],
        "underwear": ["pants"],
    }

    print("Topological order:", topological_sort(graph))
