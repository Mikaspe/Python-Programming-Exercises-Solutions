rowsNum, colNum = map(int, input('Type dimensions as rows,columns: ').split(','))

array = [[i*j for j in range(colNum)] for i in range(rowsNum)]

print(array)


