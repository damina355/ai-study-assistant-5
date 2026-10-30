# Student Management System

students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student's name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudents:")
            for i in range(len(students)):
                print(i + 1, ".", students[i])

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")