# Check Question-6 for maybe better solution with 'for' function

NumInList = input('Pick numbers:').split(',')

print(NumInList, tuple(NumInList))  # Values as str

for i in range(len(NumInList)):  # Conversion str to int
    NumInList[i] = int(NumInList[i])

print(NumInList, tuple(NumInList))  # Values as int
