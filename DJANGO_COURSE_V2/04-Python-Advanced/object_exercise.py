class Dog():

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    
    def calculate_human_age(self):
        return self.age * 7

Hans = Dog(name="Hans", breed="German Shepherd", age=7)

print(Hans.calculate_human_age())