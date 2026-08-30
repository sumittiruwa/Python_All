"""DSA Practice: Coin Change - Minimum Coins (Dynamic Programming)"""


def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for value in range(coin, amount + 1):
            dp[value] = min(dp[value], dp[value - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(f"Minimum coins to make {amount}:", coin_change(coins, amount))

    amount = 3
    coins = [2]
    print(f"Minimum coins to make {amount} using {coins}:", coin_change(coins, amount))
