# Day 8
# Tuple: is a collection of data which is ordered and immutable(cannot be changed once declared)
#example
# t = (10,20,20,40)
# print(type(t))
# #tuple with differnt data types
# t= (1, "python", 3.5, True)
# print(t)

#tupe with single element

# t = (5,)  # Comma makes it tuple
# print(type(t))

#indexing in tuple
# color = ("red","blue","orange","yellow")
# print(color[3])

#slicing in tuple
# color = ("red","blue","orange","yellow","white")
# print(color[1:4])
# print(color[:3])
# print(color[2:])
# print(color[::-1])

#Tuple is immutable
# t=(10, 30, 60, 80)
# print(t[0]) #output:10
# t[0]=20 #throws error
# #no append,remove,insert allowed

# Methodss in tuple
#count():returns how many times an element appeared in tuple
# index(): returns index of element
# t =(10, 30,60,80,60,40,60)
# print(t.count(10))
# print(t.index(60))
#print(len(t))

#looping through tuple
# color = ("red", "blue", "orange", "yellow", "white")
# for items in color:
#     print(items,end="  ")

#operations in tuple
#concatenation
# t1 = (1,3,5)
# t2=(2,4,5)
# print(t1+t2)

#repetition
# t = (6, 7)
# print(t*3)

#membership
# t =(10,20,30)
# print(20 in t)
# print(40 in t)

#unpacking:assigns element to a variable
# t = (100, 200, 300,400)
# a, b, c,d =t
# print(a)
# print(b)
# print(c)
# print(d)

#converting list to tuple and vice versa
# lst = [1,2,4]
# print(type(lst))
# t=tuple(lst)
# print(type(t))

# tpl = (10,20,30)
# print(type(tpl))
# lst1 =list(tpl)
# print(type(lst1))

# Set: 
"""
collection of unique elements
it is unordered(inexing is not possible)
mutable(can be changed)
written using {}
"""

# s = {10, 20, 30, 40}
# # print(type(s))
# # print(s)

# for i in s:
#     print(i)
# #checking if element exist or not
# if 10 in s:
#     print("Yes it exists")
# else:
#     print("No it doesn't")
# #add(): add new element
# s.add(50)
# print(s,end=" ")

# #update():
# s.update([60,40,80,90])
# print(s)

# #remove():
# s.remove(40)
# print(s)

# # discard():
# s.discard(50)
# print(s)

# #pop: removes random element
# s.pop()
# print(s)

# # clear:
# s.clear()
# print(s)
# #union()
# a={1,2,3,4}
# b={3,4,5,6}
# print(a.union(b))
# print(a | b)

# #intersection
# a={1,2,3,4}
# b={3,4,5,6}
# print(a.intersection(b))
# print(a & b)

# # difference
# print(a.difference(b))
# print(a-b)

# # issubset()
# a = {3,4}
# b = {1,2,3,4}
# print(a.issubset(b))

# #issuperset()
# print(b.issuperset(a))

# #isdisjoint()
# print(b.isdisjoint(a))