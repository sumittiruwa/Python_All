def train_model(epochs):
    for i in range(1, epochs + 1):
        print(f"Epoch {i} completed")

    print("Training Finished")

# Input number of epochs
epochs = int(input("Enter number of epochs: "))

# Call the function
train_model(epochs)