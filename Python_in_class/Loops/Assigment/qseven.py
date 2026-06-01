# Recursive function to calculate total images
def total_images(data):
    total = 0

    for value in data.values():
        if isinstance(value, dict):
            total += total_images(value)  # Recursive call
        else:
            total += value

    return total

# Dataset
dataset = {
    "train": {
        "cats": 500,
        "dogs": 450
    },
    "test": {
        "cats": 120,
        "dogs": 130
    }
}


result = total_images(dataset)
print("Total number of images:", result)