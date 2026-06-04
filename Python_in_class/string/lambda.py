# lambada for string transformation
upper = lambda s: s.upper()
print(upper("kingkong"))

#sorting  string by length

words = ["python", "java", "c++", "ruby", "javascript"]
words.sort(key=lambda w: len(w))
print(words)

#using map() with lambda 

names = ["alice", "bob", "zharlie", "dave"]
titled = list(map(lambda n: n.title(), names))
print(titled)


# filter: words longer than 4 cahr
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)