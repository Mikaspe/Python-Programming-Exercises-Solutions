class Shape:
    def __init__(self):
        pass

    def area(self):
        return 99


class Square(Shape):
    def __init__(self, l=0):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length * self.length


print(Shape().area())
print(Square().area())

Asqr = Square(5)
print(Asqr.area())
