import json
import os

TODO_FILE = "todo_list.json"

def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_todo_list(todo_list):
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file)

def add_task(task):
    todo_list = load_todo_list()
    todo_list.append({"task": task, "completed": False})
    save_todo_list(todo_list)
    print(f"Added task: {task}")

def list_tasks():
    todo_list = load_todo_list()
    if not todo_list:
        print("No tasks found!")
    else:
        for i, task in enumerate(todo_list, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. [{status}] {task['task']}")

def complete_task(task_number):
    todo_list = load_todo_list()
    if 0 < task_number <= len(todo_list):
        todo_list[task_number - 1]["completed"] = True
        save_todo_list(todo_list)
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    todo_list = load_todo_list()
    if 0 < task_number <= len(todo_list):
        deleted_task = todo_list.pop(task_number - 1)
        save_todo_list(todo_list)
        print(f"Deleted task: {deleted_task['task']}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to complete: "))
            complete_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
