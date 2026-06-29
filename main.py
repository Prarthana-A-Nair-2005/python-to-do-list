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
        print("Your Tasks:")
        print(tasks)

    elif choice == "2":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "3":
        print("Marking Task as Completed...")

    elif choice == "4":
        print("Deleting a Task...")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")