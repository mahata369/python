def student(**data):#data is stored as dictionary here
    print(data)
    print(type(data))
    for k,v in data.items():
        print(k,":", v)

student(name="Ram",age=20)
student(name="Ram",age=20,city="Dhangadhi")