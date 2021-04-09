class MyClass:
    def generator(self,n):
        # values = (i for i in range(n+1) if i % 7 == 0)
        for i in range(n+1):
            if i % 7 == 0:
                yield i


Gen = MyClass()
generator = Gen.generator(int(input('Insert a number: ')))

for i in generator:
    print(i)