from shapes import Circle, Rectangle, Triangle

circle = Circle(radius=20)
rect = Rectangle(length=10,
                 height=5)
tri = Triangle(base=5,
               height=6)
print("Area Of Circle : ",circle.area()," meter^2")
print("Area Of Rectange : ",rect.area()," meter^2")
print("Area Triangle : ",tri.area()," meter^2")