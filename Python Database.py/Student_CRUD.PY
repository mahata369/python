from db_connection import connect_db

def add_student():
    try:
        conn=connect_db()

        if conn is not None:
            cursor=conn.cursor()
            name = input("Enter name ")
            age = int(input("Enter age"))
            city = input("Enter city ")

            sql = "INSERT INTO students(name,age,city) VALUES(%s,%s,%s)"
            cursor.execute(sql,(name,age,city))
            conn.commit()

            print("Student added sucessfully")

    except Exception as e:
        print("Error occured while adding student",e)

    finally:
        cursor.close()
        conn.close()

                    
    
def view_student():
    try:
        conn =connect_db()
        if conn is not None:
            cursor = conn.cursor()

        cursor.execute("Select*from students")
        records= cursor.fetchall()
        print(records)
        print("\nID\tName\tAge\tCity")
        for row in records:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
    
    except Exception as e:
        print("Error occured while fetching data ", e)
    
    finally:
        cursor.close()
        conn.close()

    
def update_student():
    try:
        conn = connect_db()
        if conn is not None:
            cursor = conn.cursor()

            sid=int(input("Enter student id to be updated"))
            city=input("Enter city to be updated")

            sql = "UPDATE students SET city=%s WHERE id=%s"
            cursor.execute(sql,(city,sid))
            conn.commit()

            if cursor.rowcount==0:
                print("Student not found")
            else:
                print("Student updated successfully")

    except Exception as e:
        print("Error occured while updating  student", e)

    finally:
        cursor.close()
        conn.close()



def delete_student():
    try:
        conn = connect_db()
        if conn is not None:
            cursor = conn.cursor()

            sid=int(input("Enter student id to be deleted"))
            

            sql = "DELETE FROM  students  WHERE id=%s"
            cursor.execute(sql, (sid,))
            conn.commit()

            if cursor.rowcount==0:
                print("student not found")
            else:
                print("Student deleted sucessfully")

    except Exception as e:
        print("Error occured while deleting  data", e)

    finally:
        cursor.close()
        conn.close()
    
def search_student():
    try:
        conn = connect_db()
        if conn is not None:
            cursor = conn.cursor()

            name=(input("Enter name to be search"))
            

            sql = "SELECT*FROM students WHERE name=%s"
            cursor.execute(sql, (name,))
            result = cursor.fetchall()

            if len(result)==0:
                print("No record found")
            else:
                print("\nID\tName\tAge\tCity")
                for row in result:
                    print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")
        

    except Exception as e:
        print("Error occured while searching  student",e)

    finally:
        cursor.close()
        conn.close()

while True:
    print("-----Student CRUD-----")
    print("\n1.Add student")
    print("2.View student")
    print("3.Update student")
    print("4.Delete student")
    print("5.Search student")
    print("6.Exit")

    choice=int(input("Enter choice:"))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        search_student()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice")