class Circle:
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    def calculate_area(self):
        print(3.1416 * (self.radius ** 2))

    def calculate_perimeter(self):
        print(2 * 3.1416 * self.radius)

circle = Circle("Red", 5)
circle.calculate_perimeter()