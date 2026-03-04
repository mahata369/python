# import mysql.connector

# def connect_db():
#     try:
#         conn=mysql.connector.connect(
#             host="localhost", user="root", password="369369#", database="collage"

#         )
#         return conn
#     except Exception as e:
#         print("Database connection error:", e)
#         return None

# It is another Custom Database Module to connect to the database
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="369369#",
        database="family"
    )