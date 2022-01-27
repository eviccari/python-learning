class Point:
    default_color = "red" # class level

    def __init__(self, x, y):
        self.x = x # instance level
        self.y = y # instance level

    @classmethod # class method
    def zero(cls):
        return cls(0, 0)

    def __str__(self):
        return f"(Point {self.x}, {self.y})"


    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(2, 5)        
""" print(type(point))
print(isinstance(point, Point))
point.draw()
point.z = 15
print(point.z)
print(Point.default_color)
print(point.default_color) """

new_point = Point.zero()
#print(f"{new_point.x} {new_point.y}")
print(str(point)) # magic methods


