tasks = []
completed_count = 0
pending_count = 0

while True:
    task_name = input("Enter task name (enter 'done' to finish): ")
    if task_name.lower() == 'done':
        break

    status_input = input("Enter task status (0 for pending, 1 for completed): ")
    if status_input.lower() == 'done':
        break

    try:
        status = int(status_input)
        if status not in [0, 1]:
            print("Invalid status. Please enter 0 for pending or 1 for completed.")
            continue
    except ValueError:
        print("Invalid input. Please enter a numerical value for status.")
        continue

    task_entry = f"{task_name}:{status}"
    tasks.append(task_entry)

    if status == 1:
        completed_count += 1
    elif status == 0:
        pending_count += 1

print("Tasks and Their Statuses:")
for task in tasks:
    print(f"- {task}")

print(f"Total Completed Tasks: {completed_count}")
print(f"Total Pending Tasks: {pending_count}")
