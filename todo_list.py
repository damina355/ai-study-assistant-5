# To-Do List

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")