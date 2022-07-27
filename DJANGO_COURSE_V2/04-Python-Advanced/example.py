# def divider(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("Please do not divide by zero!")


from os import name


class Student():
    planet = "Earth" # class object attribute. Every Student object has this attribute
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa



student1 = Student(name="Peter", gpa="4.0")
student2 = Student(name="David", gpa="4.0")
student3 = Student(name='Jenny', gpa="3.0")
student4 = student3

# print(student1.gpa, student1.name)
print(student3)

print(student1.planet)