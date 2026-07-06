# Write to the file
f = open("data.txt", "w", encoding="utf-8")
f.write("Machine Learning\n")
f.write("Deep Learning")

f.close()

# Method 2: Using with statement to read the file
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())