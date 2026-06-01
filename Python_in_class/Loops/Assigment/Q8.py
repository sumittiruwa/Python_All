# Global variable
experiment_count = 0

# Function to run an experiment
def run_experiment():
    global experiment_count
    experiment_count += 1
    print("Experiment completed.")

# Function to show total experiments
def show_count():
    print("Total experiments performed:", experiment_count)

# Function to demonstrate local scope
def local_scope_demo():
    experiment_count = 100  # Local variable
    print("Local experiment_count:", experiment_count)

# Run experiments
run_experiment()
run_experiment()
run_experiment()

# Show global count
show_count()

# Demonstrate local scope
local_scope_demo()

# Show global count again
show_count()