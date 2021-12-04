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