
class Person:
    def __init__(self, name): #This is a constructor in py with __init__
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Cena")
john.talk()

bob = Person("Bob Protector")
bob.talk()

