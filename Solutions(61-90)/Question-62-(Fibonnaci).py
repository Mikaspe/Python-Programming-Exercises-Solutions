def fun(n):

    if n > 1:
        return fun(n-1) + fun(n-2)
    elif n==1:
        return 1 + fun(n-1)
    elif n==0:
        return 0

n = int(input('n: '))

ls = [str(fun(x)) for x in range(0, n)]
print(','.join(ls))
