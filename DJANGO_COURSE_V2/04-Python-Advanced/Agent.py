from os import name


class Dog():

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog1 = Dog(name="Hans", breed="German Shepherd")
dog2 = Dog(name="Lou", breed="Labrador")

print(f"{dog1.name} and {dog2.name} are friends")