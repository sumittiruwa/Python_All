import os

def count_files(path):
    total = 0

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            total += 1
        else:
            total += count_files(full_path)

    return total

folder = input("Enter folder path: ")
print("Total files:", count_files(folder))