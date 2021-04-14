def fun(n):

    return fun(n-1) + 100 if n!=0 else 0


n = int(input('n: '))

print(fun(n))