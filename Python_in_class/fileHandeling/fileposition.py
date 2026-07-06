with open("data.txt", "w", encoding="utf-8") as f:
    f.write("ABCDEGHIiujhyh ")
    
with open("data.txt","r", encoding="utf-8")as f:
    print(f.tell())
    print(f.read(3))
    print(f.tell())
    
    f.seek(0)
    print(f.read(3))
    
    f.seek(8)
    print(f.read())