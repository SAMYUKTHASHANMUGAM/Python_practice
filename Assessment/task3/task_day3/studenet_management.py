class Student:

    def __init__(self, student_id, course, marks): #constructor
        self.student_id = student_id 
        self.course = course
        self.marks = marks

    def __str__(self): #dunder string
        return f"ID: {self.student_id}, Course: {self.course}, Marks: {self.marks}"

    def update(self, course, marks):
        self.course = course
        self.marks = marks


class student_management:

    def __init__(self):
        self.students = {}  # {id: Student object}

    #adding new students records
    def add_student(self):
        student_id = input("Enter Student ID: ")
        #check the student id already exist or not
        if student_id in self.students:
            print("Student ID already exists.\n")
            return
        else:
            course = input("Enter Course: ")
            marks = float(input("Enter Marks: "))
            self.students[student_id] = Student(student_id, course, marks)
        print("Student added successfully.\n")

    #to view the students records
    def view_students(self):
        #check for student records 
        if not self.students:
            print("No student records found.\n")
        else:
            for student in self.students.values():
                print(student)
            print()

    #update the student records

    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        #check for student id already exists or not
        if student_id in self.students:
            course = input("Enter new Course: ")
            marks = input("Enter new Marks: ")
            self.students[student_id].update(course, marks)
            print("Student updated successfully.\n")
        else:
            print("Student not found.\n")

    #delete the student record

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        #check for the student id
        if student_id in self.students:
            del self.students[student_id] #delete command
            print("Student deleted successfully.\n")
        else:
            print("Student not found.\n")


def main():
    sms = student_management()
    while True:
        print("------ Student Management System ------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            sms.add_student()
        elif choice == '2':
            sms.view_students()
        elif choice == '3':
            sms.update_student()
        elif choice == '4':
            sms.delete_student()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
    