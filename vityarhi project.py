import json
from datetime import datetime

TASK_FILE = "tasks.json"
tasks = []


def load_tasks():
    global tasks
    try:
        with open(TASK_FILE, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []


def save_tasks():
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved successfully.\n")


def add_task():
    title = input("Enter task title: ")
    description = input("Enter description: ")
    priority = input("Enter priority (High/Medium/Low): ")
    deadline = input("Enter deadline (YYYY-MM-DD HH:MM): ")

    task = {
        "title": title,
        "description": description,
        "priority": priority,
        "deadline": deadline
    }

    tasks.append(task)
    print("Task added successfully.\n")


def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: ")) - 1

    if 0 <= index < len(tasks):
        tasks.remove(tasks[index])
        print("Task deleted.\n")
    else:
        print("Invalid task number.\n")


def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['title']} | {task['priority']} | Deadline: {task['deadline']}")
    print()


def sort_by_deadline():
    try:
        tasks.sort(key=lambda x: datetime.strptime(x["deadline"], "%Y-%m-%d %H:%M"))
        print("Tasks sorted by deadline.\n")
    except ValueError:
        print("Error: Invalid date format.\n")


def sort_by_priority():
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    tasks.sort(key=lambda x: priority_order.get(x["priority"], 4))
    print("Tasks sorted by priority.\n")


def main():
    load_tasks()

    while True:
        print("==== SMART TO-DO LIST ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Sort by Deadline")
        print("5. Sort by Priority")
        print("6. Save Tasks")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            sort_by_deadline()
        elif choice == "5":
            sort_by_priority()
        elif choice == "6":
            save_tasks()
        elif choice == "7":
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()