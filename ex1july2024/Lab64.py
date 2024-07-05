#Polymorphism
#Same method can have different forms
#Same method behaves differently
class Shape:
    def area(self):
        print("Area of a shape")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return "Rectangle",self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self .radius = radius

    def area(self):
        return "Circle", 3.14*self.radius*self.radius

shape1 = Rectangle(1,2)
print(shape1.area())
shape2 = Circle(4)
print(shape2.area())