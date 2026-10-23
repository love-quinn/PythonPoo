# Class Declaration
class Student:
    """
    This class represents a student with a name and age. It provides methods to celebrate a birthday and to display a message about the student.

    To create an instance of the Student class, you need to provide a name and age as arguments to the constructor.
    student = Student("Name", Age)
    """
    def __init__(self, n, a): # Constructor Method
        # Instance Attributes
        self.name = n
        self.age = a

    # Instance Methods
    def birthday(self):
        self.age = self.age + 1

    def __str__(self):
        return f"{self.name} is a student and is {self.age} years old."

    def __getstate__(self):
        return f"Name: {self.name}, Age: {self.age}"

# Object Declarations
# s1 = Student("Liam", 24)

s2 = Student("Olivia", 32)
# s2.birthday()
print(s2.__dict__) # Attribute
print(s2.__getstate__()) # Method
print(s2.__class__) # Class