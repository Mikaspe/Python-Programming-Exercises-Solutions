class MyClass:
    name = 'DefaultName'

    def __init__(self, name=None):
        self.name = name


user1 = MyClass
print(user1.name)

user2 = MyClass
user2.name = 'Andrzej'
print(user2.name)