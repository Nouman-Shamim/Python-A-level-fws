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

# A container class that uses composition
class ShapeCollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):  # Ensuring it's a Shape instance
            self.shapes.append(shape)

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()
        return total

# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Create a ShapeCollection instance and add shapes
collection = ShapeCollection()
collection.add_shape(circle)
collection.add_shape(rectangle)

# Calculate total area of shapes in the collection
print(f"Total area of shapes: {collection.total_area()}")  # Output: Total area of shapes: 102.5
