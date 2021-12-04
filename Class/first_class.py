# program to create a class
class Student:
    name1 = "Bandhan"
    rollno = 8
    def details(self):
        print(self.name1)
        print(self.rollno)

stuobj = Student()
print(stuobj.rollno)
stuobj.details()

#   __init__ method : __init__ method in python is similar to constructor in c++ or java
class Customer:
    def __init__(self,name):
        self.name = name
    def detail(self):
        print(self.name)

customerobj = Customer("Himanshu")
customerobj.detail()