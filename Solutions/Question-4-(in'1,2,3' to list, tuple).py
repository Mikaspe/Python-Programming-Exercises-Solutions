NumInList = input('Pick a number:').split(',')

print(NumInList, tuple(NumInList))  # Values as str

for i in range(len(NumInList)):  # Conversion str to int
    NumInList[i] = int(NumInList[i])

print(NumInList, tuple(NumInList))  # Values as int
