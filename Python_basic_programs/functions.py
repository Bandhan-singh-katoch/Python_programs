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
def funarg(*args):
    print(args[3])

funarg("Aryan", "Bandhan", "Charan", "Don")


