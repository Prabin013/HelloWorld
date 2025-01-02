# PRACTICE
# WRITE A PROGRAM TO REMOVE THE DUPLICATES IN A LIST
duplicates_List = [5, 2, 3, 6, 6, 5, 2, 7, 8, 9]
uniques = []
for number in duplicates_List:
    if number not in uniques:
        uniques.append(number)

print(uniques)