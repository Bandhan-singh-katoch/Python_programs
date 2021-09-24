# functions
# creating a function
def fun():
    print("I am function")

# calling a function
fun()

# -------------  function created with parameters ---------------------#

def oddeven(num):
    if num%2 == 0:
        print("even")
    else:
        print("odd")

oddeven(3)
oddeven(8)

# ----------------- default arguments --------------------
def printnum(x, y = 4):
    print("x = ", x)
    print("y = ", y)

printnum(2)

# -------------- Keyword arguments ------------------------
def student(name , branch):
    print(name)
    print(branch)

student(name= "Bandhan", branch= "CSE")
student(branch="Civil", name="Aquib")

# ============== variable length arguments ( *args and **kwargs ) =========
#  *args : It allows us to pass the variable number of non keyword arguments to a function.
def funarg(*args):
    for item in args:
        print(item,end=" ")

name_list = ["Aryan", "Bandhan", "Charan", "Don"]
funarg(*name_list)

# Another example:
print()
def myFun(arg1, *argv):
    print("arg1 = ",arg1)

    print("*argv = ")
    for i in argv:
        print(i,end=" ")

myFun("Hello","I","am","Bandhan","Singh")



