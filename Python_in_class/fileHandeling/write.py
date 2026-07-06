students = [
    ("Subodh", 98),
    ("Sachin", 89),
    ("Sarita", 90),
    ("Krishna", 79),
    ("Rahul", 67)
]

# 1. write() - manual newlines
with open("results.txt", "w", encoding="utf-8") as f:
    f.write("===== Exam Results =====\n")

    for name, score in students:
        f.write(f"{name}: {score}\n")


# 2. writelines() - list of strings
lines = [f"{name}: {score}\n" for name, score in students]

with open("results2.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)


# 3. print() to file - simplest
with open("results3.txt", "w", encoding="utf-8") as f:
    for name, score in students:
        print(f"{name}: {score}", file=f)