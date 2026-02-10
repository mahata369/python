# Student CRUD system using exception(try,except)
import os

FILE_NAME = "data.txt"

def add_student():
    try:
        name = input("Enter name: ").strip().title()
        age = int(input("Enter age: "))
        city = input("Enter city: ").strip().title()

        if not name or not city:
            print("Name and city cannot be empty")
            return
        
        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{age}, {city}\n")

        print("Student added successfully")

    except ValueError:
        print("Age must be a number")

def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.read()
            if not data.strip():
                print("No records found")
            else:
                print("\n---Student Records---")
                print(data)
    
    except FileNotFoundError:
        print("File not found")

def update_student():
    try:
        target = input("Enter name to update: ").strip().title()
        found = False

        with open(FILE_NAME ,"r") as file, open("temp.txt","w") as temp:
            for line in file:
                if line.startswith(target + ","):
                    age =int(input("Enter new age: "))
                    city = input("Enter new city: ").strip().title()
                    temp.write(f"{target} , {age} , {city}\n")
                    found = True
                else:
                    temp.write(line)

        if found:
              os.remove(FILE_NAME)
              os.rename("temp.txt", FILE_NAME)
              print("Student updated sucessfully ")
        else:
            os.remove("temp.txt")
            print("Student not found")

    except FileNotFoundError:
        print("File not fouund ")
    except ValueError:
        print("Invalid input ")

def delete_student():
    try:
        target = input("Enter name to delete: ").strip().title()
        found = False

        with open(FILE_NAME, "r") as file, open("temp.txt", "w") as temp:
            for line in file:
                if line.startswith(target + " ,"):
                    found = True
                    continue
                temp.write(line)

        if found:
            os.remove(FILE_NAME)
            os.rename("temp.txt", FILE_NAME)
            print("Student deleted sucessfully ")
        else:
            os.remove("temp.txt")
            print("Student not found")

    except FileNotFoundError:
        print("File not found")
    
def main():
        while True:
            print('''
======= STUDENT CRUD MENU ======
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
===================================                                                                                      
''')
            choice = input("Enter choice (1-5): ").strip()

            if choice == "1":
                add_student()
            elif choice == "2":
                view_students()
            elif choice == "3":
                update_student()
            elif choice == "4":
                delete_student()
            elif choice == "5":
                print("Exiting program")
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    main()


