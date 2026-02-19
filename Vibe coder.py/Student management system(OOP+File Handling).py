
class Student:
    def __init__(self, sid, name, age, marks):
        self.sid = sid
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"{self.sid} | {self.name} | {self.age} | {self.marks}")

class StudentManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename

    def add_student(self):
        sid = input("Enter ID: ")
        name = input("Enter name: ").title()
        age = input("Enter Age: ")
        marks = input("Enter Marks: ")

        student = Student(sid, name, age, marks)

        with open(self.filename, "a") as f:
            f.write(F"{student.sid},{student.name},{student.age},{student.marks}\n")

        print("Student added sucessfully")


    # View Students
    def view_students(self):
     try:
        with open(self.filename, "r") as f:
            for line in f:
                sid, name, age, marks = line.strip().split(",")
                student = Student(sid, name, age, marks)
                student.display()
     except FileNotFoundError:
        print("No data found")


    
# Search Student

    def search_student(self):
     target = input("Enter namr to search: ").title()

    with open(self.filename, "r") as f: # type: ignore
        found = False
        for line in f:
            sid, name, age, marks = line.strip().split(",")
            if name == target:
                Student(sid, name, age, marks).display()
                found = True

        if not found:
            print("Student not found")


# Delete Student
    def delete_student(self):
        target = input("Enter name to delete: ").title()

    try:
        with open(self.filename, "r") as f:
            lines = f.readlines()

        with open(self.filename, "w") as f:
            found = False
            for line in lines:
                sid, name, age, marks = line.strip().split(",")
                if name != target:
                    f.write(line)
                
                else:
                    found = True

        if found:
            print("Student deleted")

        else:
            print("Student not found")

    except FileNotFoundError:
        print("No data found")



# Main menu
def main():
    manager = StudentManager()

    while True:
        print("\n==== Student Management ====")
        print("1. Add student")
        print("2. View Students")
        print("3. Search Student")
        print("4.Delete student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            print("Goodbye ")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()







    