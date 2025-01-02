
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']


numbers = [2,6,4,8,2,9,11]
max = numbers[0]
for n in numbers:
    if n > max:
        max = n
print(max)

# 2D List
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[2][1])
print("loop of the 2D List")
print(matrix) #this prints the whole list as it is, it includes the brackets and all

for row in matrix:
    for item in row:
        print(item) #but this one prints only the values in the list