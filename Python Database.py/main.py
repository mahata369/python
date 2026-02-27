# pip install mysql-connector-python

import mysql.connector

# Step 1: establish connection
conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="369369#",
    database="school"
)
if conn:
    print("connected to database")
else:
    print("Failed to connect ")
#step2: Create cursor

cursor=conn.cursor() # used to execute sql queries and to fetch results

while True:
    print("\n1.Insert")
    print("2.View")
    print("3.Update")
    print("4.Delete")
    print("5.Exit")

    choice=int(input("Enter choice:"))

    if choice == 1:
        name = input("Enter name ")
        age = int(input("Enter age"))
        city = input("Enter city ")

        sql="INSERT INTO students (name,age,city) VALUES(%s,%s,%s)"
        cursor.execute(sql, (name,age,city))
        conn.commit() #Save changes permanently in database(insert,uodate,delete)

        print("Record inserted sucessfully")
    
    elif choice==2:
        sql="Select* from students"
        cursor.execute(sql)
        result=cursor.fetchall()
        print("ID Name Age City")

        for row in result:
            print(row)

    elif choice==3:
        sid=int(input("Enter id to be updated"))
        city = input("Enter new city:")

        sql = "UPDATE students SET city=%s WHERE id=%s"
        cursor.execute(sql,(city,sid))
        conn.commit()
        print("Record updated sucessfully")
        
    elif choice==4:
        sid=int(input("Enter id to be deleted"))
        

        sql = "DELLETE FROM students WHERE id=%s"
        cursor.execute(sql,(sid,))
        conn.commit()
        print("Record deleted sucessfully")

        
    elif choice==5:
        print("Program ended")
        break
    else:
        print("Invalid choice")

cursor.close()
conn.close()


