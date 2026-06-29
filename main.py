tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n===== YOUR TASKS =====")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n===== YOUR TASKS =====")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_number = int(input("Enter the task number to mark as completed: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1] = "✅ " + tasks[task_number - 1]
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\n===== YOUR TASKS =====")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_number = int(input("Enter the task number to delete: "))

            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(f"'{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")