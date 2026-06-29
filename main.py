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


while True:
    print("\n========== TO-DO LIST ==========")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

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
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")