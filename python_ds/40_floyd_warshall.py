"""DSA Practice: Floyd-Warshall All-Pairs Shortest Path Algorithm"""

INF = float("inf")


def floyd_warshall(graph):
    n = len(graph)
    dist = [row.copy() for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


if __name__ == "__main__":
    graph = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0],
    ]

    result = floyd_warshall(graph)
    print("All-pairs shortest distances:")
    for row in result:
        print(row)
