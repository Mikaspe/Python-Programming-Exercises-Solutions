import math

C = 50
H = 30
D = input('Type one or more values separated with comma: ').split(',')

for i in range(len(D)):
    D[i] = int(D[i])
    Q = round(math.sqrt((2*C*D[i])/H))
    print(Q,end=',')