#----------Assignment Day 6 --------

# create list of 5 fruits and display it
fruits=["apple", "banana", "mango", "cherry", "kiwi"]
print(fruits)

#print the first and last element of list
numbers=["1","2","3","4"]
print(numbers[0])
print(numbers[-1])

# take 5 numbers from user and store in list
numbers=[]
for i in range(0,5):
    num=int(input("Enter a number:"))
    numbers.insert(i, num)
print(numbers)

# add one element at 2nd position of list
name=["Anuj","Raj","Padam","Tika","Khadak"]
name.insert(1,input("Enter cast: "))
print(name)

# remove an element from list
name=["Anuj","Raj","Padam","Tika","Khadak"]
name.remove("Anuj")
print(name)

# # sort list in descending order
numbers=[1, 3, 7, 5, 9]
numbers.sort(reverse=True)
print(numbers)

# reverse a list using slicing
number=[1,2,3,4,5]
print(number[::-1])

# store at least 20 numbers in list and print only even numbers
numbers= []
for i in range(20):
     num=int(input("Enter a number:"))
     numbers.insert(i,num)
print(numbers)

for num in numbers:
     if num % 2 == 0:
          print(num)

#store at least 20 numbers in list and print only odd numbers
numbers = []
for i in range(20):
    num = int(input("Enter a number: "))
    numbers.append(num)
print(numbers)
for num in numbers:
    if num % 2 != 0:
        print(num)

# program to find largest number in list
numbers=[1,2,3,4,5,6]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Large number is:", largest)
