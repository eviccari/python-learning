class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    # magic method to check if instance attributes is equal to another 
    def __eq__(self, __o: object) -> bool: 
        return self.x == __o.x and self.y == __o.y

    # magic method to check if instance attributes is numerically greater than another
    def __gt__(self, __o: object) -> bool:
        return self.x > __o.x and self.y > __o.y

point = Point(10, 20)
other = Point(5, 10)
print(point == other)        
print(point > other)        