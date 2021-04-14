class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


rectangle = Rectangle(2, 4)
print(rectangle.area())
