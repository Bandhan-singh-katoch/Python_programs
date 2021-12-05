# program for constructor
# default constructor : that accepts no arguments.
# It has only one argument which is a reference to the instance being created.
class Student:
    def __init__(self):
        self.name = "Bandhan"
    def display(self):
        print("Name = ",self.name)

student = Student()
student.display()

# parameterized constructor : that accepts parameters
class Sum:
    a = 0
    b = 0
    sum = 0
    def __init__(self,m,n):
        self.a = m
        self.b = n

    def calculate(self):
        self.sum = self.a + self.b

    def display(self):
        print("a = ",self.a)
        print("b = ",self.b)
        print("Sum = ",self.sum)

sum = Sum(2,3)
sum.calculate()
sum.display()