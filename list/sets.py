# creating sets 

tags = {"python", "ml", "python", "ai","ml"}
print(tags)

nums = set([1,2,3,4,5,6,7,77])
print(nums)

#0(1) membership test 

vocab = set(["hello", "universe","Python"])
print("python" in vocab)
print("jave" in vocab)

# set operations 

a = {1,2,3,4,56}
b ={1,2,3,4,56}

print(a & b) # intersection
print(a | b)  #union
print(a - b)  #difference