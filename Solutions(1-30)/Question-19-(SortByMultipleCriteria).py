data = input('name, age, height: ').split()


for i in range(len(data)):
    data[i] = data[i].split(',')
    data[i][1] = int(data[i][1])
    data[i][2] = int(data[i][2])
    data[i] = tuple(data[i])

data.sort(key=lambda x: (x[0], x[1], x[2]))

print(data)
