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

# object class : in python object is root of all classes
class Child(object):
    def __init__(self,name,idno):
        self.name = name
        self.idno = idno

    def display(self):
        print(self.name)
        print(self.idno)

class Student(Child):
    def __init__(self,name,idno,school,std):
        self.school = school
        self.std = std

        Child.__init__(self,name,idno)

a = Student("Bandhan","123","GGI","3")
a.display()