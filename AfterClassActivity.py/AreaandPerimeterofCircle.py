import math

class Circle:
    radius = None

    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return self.radius * self.radius

    def getPerimeter(self):
        return self.radius*2*math.pi
    

obj = Circle(120)
print(obj.getArea())
print(obj.getPerimeter())