tasks = []


def save_tasks():
    file = open("tasks.txt", "w")

    for task in tasks:
        file.write(task + "\n")

    file.close()


def load_tasks():
    try:
        file = open("tasks.txt", "r")

        for line in file:
            tasks.append(line.strip())

        file.close()

    except FileNotFoundError:
        pass


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\n===== YOUR TASKS =====")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")


def mark_task_completed():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        view_tasks()

        try:
            task_number = int(input("Enter the task number to mark as completed: "))

            if 1 <= task_number <= len(tasks):
                if tasks[task_number - 1].startswith("✅"):
                    print("Task is already completed.")
                else:
                    tasks[task_number - 1] = "✅ " + tasks[task_number - 1]
                    save_tasks()
                    print("Task marked as completed!")

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")


def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.")
    else:
        view_tasks()

        try:
            task_number = int(input("Enter the task number to delete: "))

            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                save_tasks()
                print(f"'{deleted_task}' deleted successfully!")

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")


load_tasks()
def view_statistics():
    total_tasks = len(tasks)

    completed_tasks = 0

    for task in tasks:
        if task.startswith("✅"):
            completed_tasks += 1

    pending_tasks = total_tasks - completed_tasks

    print("\n===== TASK STATISTICS =====")
    print(f"Total Tasks      : {total_tasks}")
    print(f"Completed Tasks  : {completed_tasks}")
    print(f"Pending Tasks    : {pending_tasks}")

def search_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    keyword = input("Enter a keyword to search: ").lower()

    found = False

    print("\n===== SEARCH RESULTS =====")

    for i, task in enumerate(tasks, start=1):
        if keyword in task.lower():
            print(f"{i}. {task}")
            found = True

    if not found:
        print("No matching tasks found.")
def edit_task():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter the task number to edit: "))

        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the new task: ")

            # Keep the completed status if it exists
            if tasks[task_number - 1].startswith("✅"):
                tasks[task_number - 1] = "✅ " + new_task
            else:
                tasks[task_number - 1] = new_task

            save_tasks()
            print("Task updated successfully!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")
while True:
    print("\n========== TO-DO LIST ==========")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. view statistics")
    print("6. search tasks")
    print("7. Edit Task")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        mark_task_completed()

    elif choice == "4":
        delete_task()

   
    elif choice == "5":
        view_statistics()
    elif choice == "6":
        search_tasks()
    elif choice == "7":
        edit_task()
    elif choice == "8":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 8.")