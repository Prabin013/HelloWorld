class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

dog1 = Dog()
dog1.walk() #this is inherited from the mammal class
dog1.bark() #this one is not inherited from anywhere it is within the dog class