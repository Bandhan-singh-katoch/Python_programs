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
