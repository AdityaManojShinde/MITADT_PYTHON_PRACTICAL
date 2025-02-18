class Shape:
    def __init__(self, length=None, height=None, radius=None):
        self.length = length
        self.height = height
        self.radius = radius

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(length=None, height=None, radius=radius)  # Explicitly passing None
    def area(self):
        return 3.14 * (self.radius**2)
    
class Rectangle(Shape):
    def __init__(self, length, height):
        super().__init__(length=length, height=height, radius=None)  # Explicitly passing None
    def area(self):
        return self.length * self.height
    
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(length=None, height=height, radius=None)  # Pass only height
        self.base = base
    def area(self):
        return 0.5 * self.base * self.height