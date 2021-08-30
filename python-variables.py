import constant

# Assigning multiple values to multiple variables
a, b, c = 3, 2.4, "Hello"
print(a)
print(b)
print(c)

# assigning same value to different variables
a = b = c = "Bandhan"
print(a)
print(b)
print(c)

# accessing constants from constant.py file
print(constant.PI)
print(constant.NAME)


# Literals: Literal is a raw data given to the variables to constant
# Boolean literal
x = (1 == True)
y = (1 == False)
a = 1 + True
b = 4 + False

print(x)
print(y)
print(a)
print(b)

# Special literal
# None : used to specify that the field has not been created
btech = None
course = "cse"
if course == "cse":
    print(btech)
