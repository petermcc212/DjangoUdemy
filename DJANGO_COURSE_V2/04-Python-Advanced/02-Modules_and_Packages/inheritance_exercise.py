from nis import cat
from os import name


class Animal():

    def __init__(self, aName, aSpecies):
        self.aName = aName
        self.aSpecies = aSpecies
    
    def greet(self):
        print(f"Hi! My name is {self.name} and I am a {self.species}")


class Cat(Animal):

    def __init__(self, aName):
        Animal.__init__(self, aName, "Cat")

    def sound(self):
        print("meow")


class Dog(Animal):

    def __init__(self, aName):
        Animal.__init__(self, aName,"Dog")

    def sound(self):
        print("ruff")


    


jazz = Cat("Jazz")
jazz.sound()

