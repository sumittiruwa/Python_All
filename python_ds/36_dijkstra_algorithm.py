"""DSA Practice: Dijkstra's Shortest Path Algorithm"""

import heapq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = {
        "A": [("B", 4), ("C", 1)],
        "B": [("A", 4), ("D", 1)],
        "C": [("A", 1), ("D", 5), ("B", 2)],
        "D": [("B", 1), ("C", 5)],
    }

    print("Shortest distances from A:", dijkstra(graph, "A"))
