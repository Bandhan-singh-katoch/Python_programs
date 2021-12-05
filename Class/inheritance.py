# Inheritance
class Person:
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name
    def isEmployeed(self):
        return False

class Employee(Person):
    def isEmployeed(self):
        return True

person = Person("Geek1")
print(person.getName(),person.isEmployeed())

employee = Employee("Geek2")
print(employee.getName(),employee.isEmployeed())