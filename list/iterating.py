grades = {"krishna":90, "sachin":80, "bhupen":88, "Rahul":99}

# 1. Iterate keys ,

for name in grades:
    print(name, end="")  # names

# 2. Iterarte Values - compute average 

avg = sum(grades.values()) / len(grades)
print(f"Average: {avg:.1f}")

# 3. Iterates items - filter & display 

print("Passed Student:")
for name, score in grades.items():
          if score >=70:
              print(f"{name}:{score}")


# 4. Sort by score descending 

ranked = sorted(grades.items(), key=lambda x:x[1], reverse=True)
print("Ranking:", ranked)