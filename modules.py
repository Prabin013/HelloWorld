import converters # one way to import a module, this approach imports all the methods in the imported module
from converters import kg_to_lbs  #we can import only the needed function by ctrl + space after the key word "from the converters"
print(converters.kg_to_lbs(70))