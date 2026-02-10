import os

line_no = int(input("Enter line number to delete:"))

with open("data.txt","r") as original, open("temp.txt","w") as temp:
    for i, line in enumerate(original, start=1):
        if i != line_no:
            temp.write(line)

os.remove("data.txt")
os.rename("temp.txt","data.txt")

print("Line deleted sucessfully")