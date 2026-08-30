"""DSA Practice: Trie (Prefix Tree)"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True

    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix):
        return self._find_node(prefix) is not None

    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


if __name__ == "__main__":
    trie = Trie()
    for word in ["cat", "car", "card", "care", "dog"]:
        trie.insert(word)

    print("Search 'car':", trie.search("car"))
    print("Search 'ca':", trie.search("ca"))
    print("Starts with 'ca':", trie.starts_with("ca"))
    print("Starts with 'do':", trie.starts_with("do"))
    print("Starts with 'bat':", trie.starts_with("bat"))
