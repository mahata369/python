#student_crud.py
#sid,name,age,address

students = {}

def add_student():
    sid = input("Enter student id: ").strip()
    name = input("Enter student name: ").strip().title()
    age = input("Enter student age:").strip()
    address = input("Enter student address: ").strip().title()

    students[sid] = {"name":name, "age":age, "address":address}
    print("Student added sucessfully.")
    print(students)
    
def view_student():
    if not students:
        print("No student data found")
    
    for sid,info in students.items():
        print(f"ID:{sid}\nName:{info["name"]}\nAge:{info["age"]}\nAddress:{info["address"]}")
        print("-------")

    
def update_student():
    sid = input("Enter sid to be updated:").strip()

    if sid in students:
        print(f"Current data: {students[sid]}")
        name = input("Enter new name:").strip().title()
        age = input("Enter new age:").strip()
        address = input("Enter new address:").strip()

        students[sid] = {"name":name, "age":age, "address":address}

    else:
        print("No record found")
    
def delete_student():
    sid = input("Enter sid to be delete: ").strip()

    if sid in students:
        del students[sid]
        print("Student record deleted sucessfully")
    else:
        print("Student doesn't exist")
    


while True:
    print("\n---Student CRUD app---")
    print("1. Add student")
    print("2. View student")
    print("3. Update student")
    print("4. Delete student")
    print("5.Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        print("Exiting....")
        break
    else:
        print("Invalid choice")