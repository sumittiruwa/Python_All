txt = 'ram'

# for loop
for ch in txt:
     print(ch, end=" ")
     #enumerate 
     for i, ch  in enumerate(txt):
         print(f"{i}:{ch}", end="")
         
         # compershnsion
         
         vowels = [c for c in txt if c in "AEIOU"]
         print(vowels)