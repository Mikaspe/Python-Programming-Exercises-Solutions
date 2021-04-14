def gen(n):
    i = 0

    while i < n:
        if i%5==0 and i%7==0:
            yield i
        i += 1


n = int(input('n: '))
l = []

for i in gen(n):
    l.append(str(i))

print(','.join(l))
