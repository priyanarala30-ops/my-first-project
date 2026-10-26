import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title, priority):
    """Add a new task."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority.capitalize(),
        "status": "Pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"\nTask '{title}' added successfully!")

def view_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n--- Current Tasks ---")
    print(f"{'ID':<5} {'Title':<30} {'Priority':<12} {'Status':<10}")
    print("-" * 60)
    for task in tasks:
        print(f"{task['id']:<5} {task['title']:<30} {task['priority']:<12} {task['status']:<10}")
    print("-" * 60)

def complete_task(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks(tasks)
            print(f"\nTask {task_id} marked as completed!")
            return
    print(f"\nTask ID {task_id} not found.")

def main():
    while True:
        print("\n=== Personal Task Tracker ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            title = input("Enter task description: ").strip()
            priority = input("Enter priority (Low / Medium / High): ").strip()
            if title:
                add_task(title, priority)
            else:
                print("Task title cannot be empty.")
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: ").strip())
                complete_task(task_id)
            except ValueError:
                print("Please enter a valid numeric ID.")
        elif choice == "4":
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
