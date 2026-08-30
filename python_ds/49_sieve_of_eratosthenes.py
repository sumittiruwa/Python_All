"""DSA Practice: Sieve of Eratosthenes - find all primes up to n"""


def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False

    return [num for num, prime in enumerate(is_prime) if prime]


if __name__ == "__main__":
    print("Primes up to 50:", sieve_of_eratosthenes(50))
