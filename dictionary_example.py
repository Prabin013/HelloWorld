

customer = {
    "name": "John Smith",
    "age": 20,
    "is_verified": True
}
# print(customer["age"])

#PRACTICE
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}
outPut = ""
for character in phone:
    outPut += digits_mapping.get(character, "!") + " "
print(outPut)