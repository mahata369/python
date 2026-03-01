import mysql.connector

def connect_db():
    try:
        conn=mysql.connector.connect(
            host="localhost", user="root", password="369369#", database="collage"

        )
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None