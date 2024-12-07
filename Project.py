import json

TASK_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file)

def add_task(tasks):
    description = input("Task description: ")
    deadline = input("Deadline (optional): ")
    tasks.append({"description": description, "deadline": deadline, "completed": False})
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "✔" if task["completed"] else "✗"
            print(f"{idx}. {task['description']} (Deadline: {task['deadline'] or 'None'}) [{status}]")

def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task number to complete: ")) - 1
        if 0 <= task_id < len(tasks):
            tasks[task_id]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
