"""DSA Practice: Longest Increasing Subsequence (Dynamic Programming)"""


def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


if __name__ == "__main__":
    numbers = [10, 9, 2, 5, 3, 7, 101, 18]
    print("Length of longest increasing subsequence:", longest_increasing_subsequence(numbers))
