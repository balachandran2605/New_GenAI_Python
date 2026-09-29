# ==========================================
#       STUDENT MANAGEMENT SYSTEM
# ==========================================

students = []


# ---------- Add Student ----------
def add_student():
    print("\n===== ADD STUDENT =====")

    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")

    marks1 = float(input("Enter Python mark: "))
    marks2 = float(input("Enter SQL mark: "))
    marks3 = float(input("Enter Java mark: "))

    total = marks1 + marks2 + marks3
    average = total / 3

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    student = {
        "name": name,
        "age": age,
        "department": department,
        "python": marks1,
        "sql": marks2,
        "java": marks3,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)

    print("\nStudent added successfully!")
    print("Grade:", grade)


# ---------- Display Students ----------
def display_students():
    print("\n===== ALL STUDENTS =====")

    if len(students) == 0:
        print("No students found.")
        return

    for i, student in enumerate(students, start=1):
        print("\nStudent", i)
        print("Name       :", student["name"])
        print("Age        :", student["age"])
        print("Department :", student["department"])
        print("Python     :", student["python"])
        print("SQL        :", student["sql"])
        print("Java       :", student["java"])
        print("Total      :", student["total"])
        print("Average    :", student["average"])
        print("Grade      :", student["grade"])


# ---------- Search Student ----------
def search_student():
    print("\n===== SEARCH STUDENT =====")

    search_name = input("Enter student name: ")

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found!")
            print("Name       :", student["name"])
            print("Age        :", student["age"])
            print("Department :", student["department"])
            print("Total      :", student["total"])
            print("Average    :", student["average"])
            print("Grade      :", student["grade"])

            found = True
            break

    if not found:
        print("Student not found.")


# ---------- Delete Student ----------
def delete_student():
    print("\n===== DELETE STUDENT =====")

    delete_name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == delete_name.lower():
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# ---------- Show Top Student ----------
def top_student():
    print("\n===== TOP STUDENT =====")

    if len(students) == 0:
        print("No students available.")
        return

    top = students[0]

    for student in students:
        if student["average"] > top["average"]:
            top = student

    print("Top Student :", top["name"])
    print("Department  :", top["department"])
    print("Average     :", top["average"])
    print("Grade       :", top["grade"])


# ---------- Main Program ----------
while True:

    print("\n================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Show Top Student")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        top_student()

    elif choice == "6":
        print("\nThank you for using the program!")
        break

    else:
        print("\nInvalid choice. Please try again.")