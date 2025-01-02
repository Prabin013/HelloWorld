#Simple for loop
prices = [10, 20, 30]

total = 0

for i in prices:
    total += i
    print(f"Total: {total}")

#Nested loop example
for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")



numbers = [2, 2, 2, 7]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

