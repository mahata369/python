import os

FILE_NAME = "employee.txt"

def add_employee():
    try:
        eid = input("Enter employee ID: ").strip()
        name = input("Enter employee name: ").strip().title()
        age = input("Enter employee age: ").strip()
        address = input("Enter employee address: ").strip().title()

        with open(FILE_NAME, "a") as file:
            file.write(f"{eid},{name},{age},{address}\n")

            print("Employee added sucessfully")
    
    except Exception as e:
        print("Error:", e)
    
def view_employee():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No employee found.\n")
                return
            
            print("\n---Employee Records---")
            for line in data:
                eid, name, age, address = line.strip().split(",")
                print(f"ID: {eid} | Name: {name} | Age: {age}| Address: {address}")
            print()
    
    except FileNotFoundError:
        print("File not found")
    
def delete_employee():
    pass
def update_employee():
    pass

def main():
    while True:
        print("=== Employee Management System ===")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()