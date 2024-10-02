# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Function to calculate area of different shapes
def print_area(shape):
    print(f"The area is: {shape.area()}")

# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Using polymorphism
print_area(circle)      # Output: The area is: 78.5
print_area(rectangle)   # Output: The area is: 24
