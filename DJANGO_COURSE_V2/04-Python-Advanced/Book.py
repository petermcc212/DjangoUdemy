class Book():

# dunder methods are linked to methods in python 

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # overriding the equivalent to toString method
    def __str__(self):
        return f"{self.title} written by {self.author}"

    # overriding the length method

    def __len__(self):
        return self.pages



myBook = Book('Python rocks!', "Jose", 120)
print(myBook)

print(len(myBook))

