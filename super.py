
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape): # class Name (x) is a subclass of Shape (inheritance)
    def __init__(self, color, filled, radius):
        super().__init__(color, filled) # call the constructor of the superclass # u can think of super as Shape.__init__(self, color, filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        
class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled) # call the constructor of the superclass
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width * self.width}cm^2")

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled) # call the constructor of the superclass
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")


circle = Circle(color="orange", filled=True, radius=5)
square = Square("black", False, 10)
triangle = Triangle(color="blue", filled=True, width=8, height=6)

circle.describe()
square.describe()
triangle.describe()

# print(triangle.color)
# print(triangle.filled)
# print(f"{triangle.width}cm")
# print(f"{triangle.height}cm")


