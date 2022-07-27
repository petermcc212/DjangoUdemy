class Person():

    # constructor
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def hello(self):
        print("Hello")

    def report(self):
        print(f"I am {self.first_name} {self.last_name}") 


# This class inherits the Person class, With that, it inherits all its methods
class Agent(Person):

    #If you have more attributes that you need to add beyond what's provided by 
    # the base class, we can do this

    def __init__(self, first_name, last_name, code_name):
        # Satisfy the constructor of the superclass with: 
        Person.__init__(self, first_name, last_name)
        # for new variables introduced it's just the standard self assignment
        self.code_name = code_name


    def reveal(self, passcode):
        if passcode == 123:
            print("I am a secret agent")
        else:
            self.report() 
    
    # Overriding the report method 
    def report(self):
        print("I am here.")


x = Agent("John", "Smith", "doobie")
x.reveal(123213)
print(x.first_name)
print(x.last_name)

# y = Person("Peter", "McCreadie")
# x.report