"""
DSA Practice: Recursion
Classic recursion problems: factorial, Fibonacci, and Tower of Hanoi.
"""


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def tower_of_hanoi(n, source, auxiliary, target, moves=None):
    if moves is None:
        moves = []
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {target}")
        return moves
    tower_of_hanoi(n - 1, source, target, auxiliary, moves)
    moves.append(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target, moves)
    return moves


if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("Fibonacci sequence (first 10):", [fibonacci(i) for i in range(10)])

    print("\nTower of Hanoi with 3 disks:")
    for move in tower_of_hanoi(3, "A", "B", "C"):
        print(move)
