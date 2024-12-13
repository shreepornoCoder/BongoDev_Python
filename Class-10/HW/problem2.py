class Shape:
    def __init__(self, width, height, radius, length, base):
        self.width = width
        self.length = length
        self.height = height
        self.radius = radius
        self.base = base

class Triangle(Shape):
    def calculate_area(self):
        print("Triangle Area: ", (self.width*self.height)*0.5)

    def calculate_perimiter(self):
        print("Triangle Perimiter: ",self.width + self.height + self.base)

class Square(Shape):
    def calculate_area(self):
        print("Square Area: ", self.width ** 2)

    def calculate_perimiter(self):
        print("Square Perimiter: ", 4 * self.width)

class Circle(Shape):
    def calculate_area(self):
        print("Circle Area: ", 3.1416 * (self.radius ** 2))

    def calculate_perimiter(self):
        print("Circle Perimiter: ", 2 * 3.1416 * self.radius)

circle = Circle(0, 0, 5, 0, 0)
circle.calculate_area()
circle.calculate_perimiter()

square = Square(5, 0, 0, 0, 0)
square.calculate_area()
square.calculate_perimiter()

triangle = Triangle(6, 4, 0, 0, 0)
triangle.calculate_area()
triangle.calculate_perimiter()