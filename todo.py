
TODO_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    try:
        with open(TODO_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    """Add a new task."""
    task = input("Enter the task: ")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully4!")

def remove_task():
    """Remove a task by number."""
    tasks = load_tasks()
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(load_tasks())
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye, see you next time!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
