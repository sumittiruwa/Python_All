"""DSA Practice: Palindrome Check"""


def is_palindrome(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print("'racecar' is palindrome:", is_palindrome("racecar"))
    print("'A man a plan a canal Panama' is palindrome:", is_palindrome("A man a plan a canal Panama"))
    print("'hello' is palindrome:", is_palindrome("hello"))
