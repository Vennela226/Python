# High-Level Python Program: Student Management System

students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))
    students[roll_no] = {"Name": name, "Marks": marks}
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    print("\n--- Student Records ---")
    for roll_no, details in students.items():
        print(f"Roll No: {roll_no}, Name: {details['Name']}, Marks: {details['Marks']}")
    print()

def search_student():
    roll_no = input("Enter Roll Number to search: ")
    if roll_no in students:
        s = students[roll_no]
        print(f"Found → Name: {s['Name']}, Marks: {s['Marks']}\n")
    else:
        print("Student not found.\n")

def calculate_average():
    if not students:
        print("No students to calculate average.\n")
        return
    total = sum(s["Marks"] for s in students.values())
    avg = total / len(students)
    print(f"Average Marks: {avg:.2f}\n")

def main_menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Calculate Average Marks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            calculate_average()
        elif choice == "5":
            print("Exiting Program. Thank you!")
            break
        else:
            print("Invalid choice. Try again.\n")

main_menu()
