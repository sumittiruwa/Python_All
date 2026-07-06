with open("scores.txt", "r", encoding="utf-8") as f:
    # read() - whole file
    content = f.read()
    print(repr(content))

with open("scores.txt", "r", encoding="utf-8") as f:
    # readlines() - list of lines
    lines = f.readlines()

    scores = [int(line.split()[1]) for line in lines]

    print("Scores:", scores)
    print("Average:", sum(scores) / len(scores))