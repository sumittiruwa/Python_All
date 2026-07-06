# LIfe of a file python 


f = open("notes.py", "w")
f.write("hello , py")
f.close()

# safer -  with handeles close automatically

with open("notes.py", "r") as f:
     content = f.read()
     
     print(content)
     