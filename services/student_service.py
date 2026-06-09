import json
import os

from models.student import Student


class StudentService:

    # Constructor
    def __init__(self):
        self.file_name = "data/students.json"
        self.students = self.load_students()

    # Load Students
    def load_students(self):

        if not os.path.exists(self.file_name):
            return []

        try:
            with open(self.file_name, "r") as file:
                return json.load(file)

        except:
            return []

    # Save Students
    def save_students(self):

        with open(self.file_name, "w") as file:
            json.dump(self.students, file, indent=4)

    # Add Student
    def add_student(self):

        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        for student in self.students:
            if student["student_id"] == student_id:
                print("Student ID already exists!")
                return

        student = Student(student_id, name, age, course)

        self.students.append(student.to_dict())

        self.save_students()

        print("Student Added Successfully!")

    # View Students
    def view_students(self):

        if not self.students:
            print("No Student Record Found!")
            return

        for student in self.students:

            print("-" * 30)
            print("ID:", student["student_id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])

    # Search Student
    def search_student(self):

        student_id = input("Enter Student ID: ")

        for student in self.students:

            if student["student_id"] == student_id:

                print(student)
                return

        print("Student Not Found!")

    # Delete Student
    def delete_student(self):

        student_id = input("Enter Student ID: ")

        for student in self.students:

            if student["student_id"] == student_id:

                self.students.remove(student)

                self.save_students()

                print("Student Deleted!")

                return

        print("Student Not Found!")

    # Update Student
    def update_student(self):

        student_id = input("Enter Student ID: ")

        for student in self.students:

            if student["student_id"] == student_id:

                student["name"] = input("New Name: ")
                student["age"] = input("New Age: ")
                student["course"] = input("New Course: ")

                self.save_students()

                print("Student Updated!")

                return

        print("Student Not Found!")

    # Menu Function
    def menu(self):

        while True:

            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter Choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                print("Good Bye!")
                break

            else:
                print("Invalid Choice")