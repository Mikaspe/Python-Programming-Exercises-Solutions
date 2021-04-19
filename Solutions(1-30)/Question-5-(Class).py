class MyClass:
    """This is class for string operations"""

    def __init__(self):
        self.str = 'First use .getString method'

    def getString(self):
        self.str = input('Type a string: ')

    def printString(self):
        print(self.str.upper())


def TestForClass(ClassToTest):
    test = ClassToTest()
    print(test.__doc__)
    test.getString()
    test.printString()


TestForClass(MyClass)


