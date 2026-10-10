# Student Registration System

students = {}


def add_student():
    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter Student Name: ")
    marks = float(input("Enter Student Marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks. Marks must be between 0 and 100.")
        return

    students[student_id] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully.")


def view_students():
    if len(students) == 0:
        print("No student records found.")
        return

    print("\nStudent Records")

    for student_id, details in students.items():
        print(
            "ID:", student_id,
            "| Name:", details["name"],
            "| Marks:", details["marks"]
        )


def search_student():
    student_id = input("Enter Student ID to search: ")

    if student_id in students:
        details = students[student_id]

        print("Student found.")
        print("ID:", student_id)
        print("Name:", details["name"])
        print("Marks:", details["marks"])

    else:
        print("Student not found.")


def update_student():
    student_id = input("Enter Student ID to update: ")

    if student_id not in students:
        print("Student not found.")
        return

    new_name = input("Enter updated Student Name: ")
    new_marks = float(input("Enter updated Student Marks: "))

    if new_marks < 0 or new_marks > 100:
        print("Invalid marks. Marks must be between 0 and 100.")
        return

    students[student_id]["name"] = new_name
    students[student_id]["marks"] = new_marks

    print("Student details updated successfully.")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    if student_id in students:
        del students[student_id]
        print("Student deleted successfully.")

    else:
        print("Student not found.")


def calculate_class_average():
    if len(students) == 0:
        print("No student records available.")
        return

    total_marks = 0

    for details in students.values():
        total_marks += details["marks"]

    average = total_marks / len(students)

    print("Class Average Marks:", average)


def display_highest_performer():
    if len(students) == 0:
        print("No student records available.")
        return

    highest_id = None
    highest_name = None
    highest_marks = -1

    for student_id, details in students.items():

        if details["marks"] > highest_marks:
            highest_id = student_id
            highest_name = details["name"]
            highest_marks = details["marks"]

    print("\nHighest-Performing Student")
    print("ID:", highest_id)
    print("Name:", highest_name)
    print("Marks:", highest_marks)


while True:
    print("\nStudent Registration System")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Details")
    print("5. Delete Student")
    print("6. Calculate Class Average")
    print("7. Display Highest-Performing Student")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid input. Please enter a number from 1 to 8.")
        continue

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        calculate_class_average()

    elif choice == 7:
        display_highest_performer()

    elif choice == 8:
        print("Exiting Student Registration System.")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 8.")