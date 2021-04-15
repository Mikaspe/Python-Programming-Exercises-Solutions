numbers = [12,24,35,70,88,120,155]

ls = [x for (i,x) in enumerate(numbers) if i not in (0,4,5)]

print(ls)
