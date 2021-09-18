# ------------- Chaining comparison operator --------------
# This is used to check more than one conditions in one statements

a,b,c = 1, 3, 4
# both the below if statements are same
if a<b<c:
    print("{} < {} < {} is true".format(a,b,c))
if (a<b and b<c):
    print("{} < {} and {} < {} is true".format(a,b,b,c))