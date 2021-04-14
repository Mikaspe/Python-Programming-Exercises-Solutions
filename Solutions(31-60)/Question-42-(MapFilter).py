ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = map(lambda x: x**2, filter(lambda x: x%2==0, ls))

print(list(result))
