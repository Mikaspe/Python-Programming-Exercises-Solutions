import math

C = 50
H = 30
Q = []
D = input('Type one or more values separated with comma: ').split(',')


# First solution
# for i in range(len(D)):
#    D[i] = int(D[i])
#    Q.append(str(round(math.sqrt((2*C*D[i])/H))))

# print(','.join(Q))


# Second solution - Better IMO
for d in D:
    Q.append(str(round(math.sqrt((2*C*float(d))/H))))

print(','.join(Q))
