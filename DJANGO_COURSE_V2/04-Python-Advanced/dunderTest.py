class Students():

    def __init__(self, names):
        self.names = names

    def __len__(self):
        return len(self.names)

    def __str__(self):
        return f"{self.names}"


students = Students(["A", "B", "C"])
print(students)
# print(len(students))