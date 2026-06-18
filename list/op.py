# Dictionary operation & methods 

catalog = {"apple":1.5, "mango": 2.0, "banane":0.9}

# Dictionary comprenhension (pythonic !)

expensive = {k:v for k, v in catalog.items() if v>1.0}
print(expensive)

# MErge two dicts (python 3.9+)

extras = {"grape": 3.0, "lime":1.2}
catalog.update(extras)

# Coutn word frequency (classic NLP!)

text = "The cat sat on the mat the cat"
freq = {}

for owrd in text.split():
    freq[word] = freq.get(word,0 ) + 1
    print(freq)