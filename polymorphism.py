
# Polymorphism in Python: poly = many; morphe = form
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2 # print() only shows something to the user, but return gives a value to the program to use later

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2 # two asterisks mean to the power of x

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping
    
shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("margherita", 15)]

for shape in shapes:
    print(f"{shape.area()}cm²")
