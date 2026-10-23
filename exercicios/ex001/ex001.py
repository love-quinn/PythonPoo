# Class Declaration
class Student:
    def __init__(self): # Constructor Method
        # Instance Attributes
        self.name = ""
        self.age = 0

    # Instance Methods
    def birthday(self):
        self.age = self.age + 1

    def message(self):
        return f"{self.name} is a student and is {self.age} years old."

# Object Declarations
s1 = Student()
s1.name = "Liam"
s1.age = 24
print(s1.message())

s2 = Student()
s2.name = "Olivia"
s2.age = 32
print(s2.message())