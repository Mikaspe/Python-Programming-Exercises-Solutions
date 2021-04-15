numbers = [12,24,35,70,88,120,155]

ls = [x for (i, x) in enumerate(numbers) if i not in range(2,5)]

print(ls)