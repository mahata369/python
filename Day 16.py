#Student CRUD using file handling
def add_student():
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = int(input("Enter marks: "))

        with open("student.txt", "a") as f:
            f.write(f"{name},{age},{marks}\n")

        
    
    except ValueError:
        print("Invalid age or marks")
    except FileNotFoundError:
        print("File not found")
    else:
        print("Student added sucessfully")

def view_student():
    try:
       with open("student.txt", "r") as f:
          data = f.read
          if data == "":
            print("No record ")
          else:
             print("-----Student Data-----")
    
    except FileNotFoundError:
       print("File not found")
        
          
    
def search_student():
   try:
      search_name = input("Enter student name to search: ")
      found = False
      with open("student.txt", "r") as f:
         for line in f:
            name, age, marks = line.strip().split(",")
            if name.lower() == search_name.lower():
               print("Record...")
               print(f"Name:{name}\nAge:{age}\nMarks:{marks}")
               found = True
               break

         if not found:
            print("Name not found")
    
   except FileNotFoundError:
    print("File not found")
    
def delete_student():
    try:
       target_name = input("Enter name to be deleted")
       found = False

       with open("student.txt","r") as f:
          lines = f.readlines()
       with open("student.txt","w") as f:
          for line in lines:
            name,age,marks = line.strip().split(",")
            if name.lower() != target_name.lower():
               f.write(line)

            else:
               found = True
        
       if found:
          print("Student record deleted successfully")
       else:
          print("Record not found")

    except FileNotFoundError:
       print("File not found")

def update_student():
   try:
      target_name = input("Enter name to be updated")
      found = False

      with open("stuudent.txt","r") as f:
        lines =f.readlines()

        with open("student.txt","w") as f:
           for line in lines:
              name,age,marks =line.strip().split(",")
              if name.lower() == target_name.lower():
                 
                 print("Old Record...")
                 print(f"Name:{name}\nAge:{age}\nMarks:{marks}")

                 new_name=input("Enter new name: ")
                 new_age=int(input("Enter new age: "))
                 new_marks = int(input("Enter new marks: "))
                 f.write(f"{new_name},{new_age},{new_marks}\n")

   except ValueError:
    print("Invalid age or marks")
   except FileNotFoundError:
      print("File not found")
    

    
   
      
        

def main():
    while True:
     print("\n STUDENT MANAGEMENT SYSTEM")
     print("1. Add Student")
     print("2. View Students")
     print("3. Search Student")
     print("4. Delete Student")
     print("5. Update student")
     print("6. Exit")

     choice = input("Enter your choice: ")

     if choice == "1":
        add_student()
     elif choice == "2":
        view_student()
     elif choice == "3":
        search_student()
     elif choice == "4":
        delete_student()
     elif choice == "5":
        update_student()
     elif choice == "6":
        print("Exiting..")
        break
     else:
        print("Invalid choice")

main()
