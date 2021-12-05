# destructor : destructors are used to destroy the object, It is called when all the reference to the object have been deleted.
class Demo:
    def __init__(self):
        print("I am constructor")
    def __del__(self):
        print("I am destructor")

demo = Demo()