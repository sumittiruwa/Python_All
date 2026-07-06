import datetime

def log_event(message, filepath="app.log"):
    # Get the current date and time
    timestamp = datetime.datetime.now()
    ts_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")

    # Append the log message to the file
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"[{ts_str}] {message}\n")


# Simulate 3 training epochs
for epoch in range(1, 4):
    accuracy = 0.75 + epoch * 0.05
    log_event(f"Epoch {epoch} - Accuracy: {accuracy:.2f}")

# Read back the log
with open("app.log", "r", encoding="utf-8") as f:
    print(f.read())