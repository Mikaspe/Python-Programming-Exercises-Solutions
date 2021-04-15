ls = [12,24,35,70,88,120,155]


# Enumerate give (index,value) from list in this case
new_ls = [x for (i, x) in enumerate(ls) if i not in (0,2,4,6)]

print(new_ls)
