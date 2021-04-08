A = input('Type dimensions as rows,columns: ').split(',')

rowsNum = int(A[0])
colNum = int(A[1])

array = [[i*j for j in range(colNum)] for i in range(rowsNum)]

print(array)


