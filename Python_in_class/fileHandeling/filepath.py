form pathlib as path
import os

#pathlib - modern appraoch 

p = Path("data") / "student" /"scores.csv"
print(p)
print(p.name)
print(p.suffix)
print(p.parent)

# check and create directories 

p.parent.mkdir(paretns = True, exist_ok = True)

# file info

if p.exist():
    print(f"Size: {p.stat().st_size} bytes")
    
# list all .txt files in a directory 
for f in Path(".").glob("*.txt"):
    print(f.name)