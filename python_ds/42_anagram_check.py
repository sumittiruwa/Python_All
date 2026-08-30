"""DSA Practice: Anagram Check"""

from collections import Counter


def is_anagram(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    return Counter(word1) == Counter(word2)


if __name__ == "__main__":
    print("'listen' & 'silent':", is_anagram("listen", "silent"))
    print("'triangle' & 'integral':", is_anagram("triangle", "integral"))
    print("'apple' & 'pale':", is_anagram("apple", "pale"))
