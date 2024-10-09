class Shape:
    def area(self):
        return 0  
class Square(Shape):
    def __init__(self, length):
        self.length = length  

    def area(self):
       n = self.length ** 2  
       return n

shape = Shape()
print(f"Area of Shape: {shape.area()}")  

square = Square(4)
print(f"Area of Square: {square.area()}")  