
#LIST METHOD BASICS

numbers = [5, 2, 1, 7, 7, 7, 4]
numbers.append(30) #adds the number to the end of the list
numbers.insert(0, 12) #adds the number wherever desired just remember to indicate in the args
numbers.remove(7) #removes the specified number from the list
# numbers.clear() #clears the whole list
print(numbers.count(7))
print(numbers.index(5))
print(2 in numbers) #returns boolean, whether that particular thing is in the list or no

print(numbers)