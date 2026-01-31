Day 7
# # Day 7
# # searching

# data=[
#     ["Ram, 22,"chitwan"],
#     ["shyam", 21,"Kathmandu"],
#     ["Hari",22,"pokhara"],
#     ["Alex",22,"Butwal"],
# ]
# target_name=input("Enter name to be searched ")
# target_add =input("Enter address to be searched")

# found = false #boolean variable

# for item in data:
#     item_name=str(item[0]).lower()
#     item_address=str(item[2]).lower()

#     if item_name == target_name or item_address == target_add:
#         print(f"found record: Name: {item[0]}, Age :{item[1]}, address:{item[2]}")
#         found = True
# if not found:
#     print("No matching record found")

# ...
# target_name=seeta
# target_add=parsa

# ..Dry running..
# 1s iteration:
# ["Ram",22,"chitwan"]
# item_name=Ram
# item_name=Chitwan

# if Ram ==seeta or chitwan==parsa:not satisfied

# 2nd itetrarion:
# ["shyam",21,"kathmandu"]
# item_name=shyam
# item_name=kathmandu

# if shyam==seeta or kathmandu==parsa:not satisfied
# .
# .
# .
# upto 4th itetration it is same

# 5th itetration
# ["seeta",22,"Butwal"]
# item_name=seeta
# item_name=butwal

# if seeta==seeta or butwal==parsa:satisfied
# found record:Name:seeta, Age:22, Address:Butwal
# found=True
# ...

#List comprehisnsion

#list of square of numbers from 1-5
#normal way
# lst=[]

# for i in range (1,6):
#     lst.append(i*i)

# print(lst)


#List comprehension

# lst=[i*i for i in range(1,6)]
# print(lst)

#noramal way
# even=[]
# for i in range(1,11):
#     if i % 2 ==0:
#         even.append(i)
# print(even)


# even=[i for i in range (1,11) if i % 2 == 0]
# print(even)

# num=[1,2,3,4,5]
# sq=[x*x for x in num]
# print(sq)

#print value in uppercase
# fruits=["apple","banana" ,"mango"]
# new_list=[ fruits.upper() for fruits in fruits]
# print(new_list)


# ...
# input =[1,2,3,4,5]
# output=['odd','even','odd','even','odd']
# ...

# result=["Even" if i % 2 ==0 else "odd" for i in range (1,6)]
# print(result)

#palindrome 
# word=["madam","hello","lol","radar","level"]

# palindrome=[i for i in word if i[::-1] == i]
# print(palindrome)
