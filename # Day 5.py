# Day 5
# control flow statement
#break,continue,pass
#break:stops loop immediately upon satisfying condition
#to terminate loop if i == 5
for i in range (1,5):
    if i == 5:
         break
     print(i,end=" ")

 print("break statement executed")

#print first 5 even numbers (1,20)
count=0
for i in range(1,21):
    if i % 2== 0:
        print(i,end=" ")
        count+=1

    if count==5:
        break

#continue:skips the current itetration  and move to next itetration(next loop cycle)
# #loop doesnot stop,only current value is ignored
for i in range (1,6):
    if i==2:
        continue
    print(i,end=" ")

# #pass:placeholder  
# syntax  
#for i in range(1,6):
#     pass

#reverse a num
123, output:321
num=int(input("Enter multidigit number:"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num //=10
print(f"reversed number:{rev}") 
 
# ...
# input:123
# 1st itetration
# digit:3
# rev=o*10+3=3
# num=12
# 2nd itetration:
# digit:2
# rev=3*10+2=32
# num=1
# 3rd itetration
# digit=1
# rev=32*10+1=321
# num=1/10=1
#...

#check wheater a number is palindrome or not
#num=reverse(num)

