import re 

# NLP preprocessing pipeline

text = "hello ! , It's me mitsu"

# step 1: Normalize
text = text.lower().strip()

#step 2: Remove punctuation
text = re.sub(r'[^\w\s]', '', text)

#step 3 : Tokenize
tokens = text.split()

#step 4 : Remove stop words
stop_words = {"the", "is", "in", "and", "to", "it", "me"    }
tokens = [t for t in tokens if t not in stop_words] 

print(tokens)
