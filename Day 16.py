#Student CRUD using file handling
def add_student():
    try:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = int(input("Enter marks: "))
        
        # Creating new unique id
        new_id = 1
        try:
            with open("student.txt", "r") as f:
                lines = f.readlines()  # Read all lines, not just one
                if lines:
                    last_line = lines[-1]  # Get the last line
                    last_id = int(last_line.split(",")[0])
                    new_id = last_id + 1
        except FileNotFoundError:
            print("File not found, creating new file")
        
        # Adding data to the file
        with open("student.txt", "a") as f:
            f.write(f"{new_id},{name},{age},{marks}\n")
        
        print("Added successfully")
    
    except ValueError:
        print("Invalid input. Please enter valid age and marks (numbers)")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_student():
    try:
       with open("student.txt", "r") as f:
          data = f.read
          if data == "":
            print("No record ")
          else:
             print("-----Student Data-----")
             print(data)
    
    except FileNotFoundError:
       print("File not found")
        
          
    
def search_student():
   try:
      search_id = input("Enter student ID to search: ")
      found = False
      with open("student.txt", "r") as f:
         for line in f:
            sid,name, age, marks = line.strip().split(",")
            if sid == search_id:
               print("Record...")
               print(f"Name:{name}\nAge:{age}\nMarks:{marks}")
               found = True
               break

         if not found:
            print("Student not found")
    
   except FileNotFoundError:
    print("File not found")
    
def delete_student():
    try:
       target_id= input("Enter id to be deleted")
       found = False

       with open("student.txt","r") as f:
          lines = f.readlines()
       with open("student.txt","w") as f:
          for line in lines:
            sid,name,age,marks = line.strip().split(",")
            if sid != target_id:
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
