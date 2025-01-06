class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 10)
point1.x = 10
point1.y = 20


point2 = Point(15, 7)
point2.x = 30
point2.y = 50

point = Point(10, 20)
point.x = 11
print(point.x)