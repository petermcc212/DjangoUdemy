from cmath import pi


class Circle():

    pi = 3.14
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def perimeter(self):
        return Circle.pi * self.radius * 2

    def multiply_radius(self, number):
        self.radius = self.radius * number
        print(f'Radius has been changed to {self.radius}')

myCircle = Circle(radius=4)
myCircle.multiply_radius(12)
print (myCircle.radius)