"""
Simple To-Do App
Author: Sithum-Devops
Features:
    - Add tasks
    - Show tasks
    - Mark tasks as done
"""

tasks = []

def show_tasks():
    """Display tasks with status."""
    if not tasks:
        print("No tasks yet! Time to relax.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['task']} [{status}]")

def add_task():
    """Add a new task."""
    task_text = input("Enter a task: ").strip()
    if task_text:
        tasks.append({"task": task_text, "done": False})
        print(f"Task '{task_text}' added!")
    else:
        print("Task cannot be empty!")

def complete_task():
    """Mark a task as done."""
    show_tasks()
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to mark as done: "))
        if 1 <= idx <= len(tasks):
            tasks[idx - 1]["done"] = True
            print(f"Marked '{tasks[idx - 1]['task']}' as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    print("Welcome to your Simple To-Do App!")
    while True:
        print("\n--- Menu ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Goodbye! Have a productive day!")
            print("*"*40)
            print("/nLearn with Sithum")
            break
        else:
            print("Invalid choice. Please try 1-4.")

if __name__ == "__main__":
    main()
  
