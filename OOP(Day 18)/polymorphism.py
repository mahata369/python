# Polymorphism: means same method name but different behavior

class Shape:
    def area(self, x, y):
        print("Area of shape")

class Rectangle(Shape):
    def area(self, x, y):
        return x*y
    
class Triangle(Shape):
    def area(self, x, y):
        return (x*y) / 2
    
r = Rectangle()
print(f"Area of rectangle is : {r.area(10,5)}")
t = Triangle()
print(f"Area of triangle is: {t.area(10, 5)}")