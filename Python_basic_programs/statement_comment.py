# ...multi line statement...
# line continuation character (\)
a = 1+2+2+\
    3+9+4+3
print(a)

# or by using (),{} ,[]
a = (1+2+3
     +4+1)
print(a)

# ........python indentation.....
if True:
    print("Python indentation")

# ........Comments.........#
# this is single line comment

""" This
    is multi-line
    comment """

'''This is
    also multi-line
    comment '''

# .......docstrings.......
# documentation string that appear right after the function, class, method or module
def double(num):
    """Function to double the value"""
    return 2*num
print(double(3))
# we can access the docstring also
print(double.__doc__)