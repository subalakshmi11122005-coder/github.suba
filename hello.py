tasks = []

while True:
    print("\nTO-DO LIST")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == 2:
        print("\nTasks:")
        for i, task in enumerate(tasks, start=1):
            print(i, task)

    elif choice == 3:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted successfully!")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid Choice!")