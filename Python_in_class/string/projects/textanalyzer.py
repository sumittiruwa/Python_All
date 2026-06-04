def analyze_text(text):
    """Analyze a given text and return some statistics."""
    
    clean = text.lower().strip()
    words = clean.split()
    char = [c for c in clean if c.isalpha()]
    vowels = [c for c in char if c in 'aeiou']
    sentences = text.split('.')
    
    # word redundancy
    freq = {w: words.count(w) for w in set(words)}
    top3 = sorted(freq, key=lambda w:freq[w], reverse=True)[:3]
    
    return{
        "total_chars"  : len(text),
        "toatl_words": len(words),
        "unique_words":len(set(words)),
        "total_sentences": len([s for s in sentences if s.strip()]),
        "vowels" : len(vowels),
        "top_3_words": top3,
        "is_all_lower": text == text.lower()
    }
    
    
sample = "python is great great great among greatest . it is fun and fun an fun and fun andf una nfudnf ofkjh khskl ahndjfhlksjahgkljhlhashdkh"
result = analyze_text(sample)
for k, v in result.items():
        print(f"{k:20}: {v}")