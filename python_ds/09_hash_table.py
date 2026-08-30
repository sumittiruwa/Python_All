"""
DSA Practice: Hash Table
A simple hash table built from scratch using chaining for collision handling.
"""


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False


if __name__ == "__main__":
    table = HashTable()
    table.put("name", "Sumit")
    table.put("language", "Python")
    table.put("topic", "DSA")

    print("name ->", table.get("name"))
    print("language ->", table.get("language"))

    table.remove("topic")
    try:
        table.get("topic")
    except KeyError:
        print("topic was removed successfully")
