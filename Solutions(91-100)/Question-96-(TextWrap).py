from textwrap import wrap, fill

S = input('String: ')
W = int(input('Widght: '))

# IMO better solution
print(fill(S, W))
####################

wrapped = wrap(S, W)

for line in wrapped:
    print(line)


