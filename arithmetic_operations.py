class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # magic method to sum each attribute instance to another
    def __add__(self, __o: object) -> object:
        return Point(self.x + __o.x, self.y + __o.y)

    #override base __str__ method 
    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

point = Point(10, 15)
another = Point(1, 2)
combined = (point + another)        
print(str(combined))