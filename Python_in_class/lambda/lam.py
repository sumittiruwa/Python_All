# Simple task list
tasks = [
    {"title": "Finish UI design", "completed": True},
    {"title": "Learn Python", "completed": False},
    {"title": "Build portfolio", "completed": False},
    {"title": "Push to GitHub", "completed": True}
]

# Use lambda to filter completed tasks
completed_tasks = list(filter(lambda task: task["completed"] == True, tasks))

print("Completed Tasks:")
for task in completed_tasks:
    print(task["title"])