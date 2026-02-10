# Exception: an error that occurs during program execution
'''
Types of error:
     Syntax error
     Runtime error
     Logical error
'''

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))

# try:
#     print(a/b)
# except:
#     print("Error:Cannot divide by zero")


# try:
#     f = open("abc.txt", "r")
#     print(f.read())
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("Permission denied")

try:
    n = int(input("Enter a number "))#Exception generation codes
    print(100/n)

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("No error")

finally:
    print("this is finally block")

