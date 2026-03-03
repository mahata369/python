from db_connection import get_connection

# Insert function
def insert_members(name, age, relation, location):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO members (name,age,relation,location) VAlUES (%s, %s, %s,%s)"
    values = (name,age, relation,location)

    cursor.execute(sql, values)
    conn.commit()

    print("Member inserted sucessfully!")

    cursor.close()
    conn.close()

# View functin
def view_members():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute ("SELECT * FROM members")
    records = cursor.fetchall()

    for row in records:
        print(row)

    cursor.close()
    conn.close()

# UPDATE function
def update_members(mid, location):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "UPDATE members SET location = %s WHERE id = %s"
    values = (location,mid)

    cursor.execute(sql, values)
    conn.commit()

    print("Record updated sucessfully!")

    cursor.close()
    conn.close()

# DELETE function
def delete_member(mid):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "DELETE FROM members WHERE id = %s"
    cursor.execute(sql, (mid,))
    conn.commit()

    print(" Record deleted successfully!")

    cursor.close()
    conn.close()

# USER interface
while True:
    print("----Family CRUD----")
    print("1. Insert members")
    print("2. View members")
    print("3. Update members")
    print("4. Delete members")
    print("5. EXIT")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        relation = input("Enter relation: ")
        location=input("Enter location: ")
        insert_members(name,age,relation,location)

    elif choice == 2:
        view_members()

    elif choice == 3:
        mid = int(input("Enter member id to update: "))
        location = input("Enter new location: ")
        update_members(mid, location)
    
    elif choice == 4:
        mid =int(input("Enter member id  to delete:"))
        delete_member(mid)
    
    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
