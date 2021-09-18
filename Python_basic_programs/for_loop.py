# =================  for loop =====================
# for loop is used for the sequential iteration i.e. used for iterating over the iterable like tuple, list, string
# SYNTAX:  for var in iterable:
               # statements

# iterating over a list
print("List iteration")
l = ['i','am','in','list']
for i in l:
    print(i)

# iteration over a tuple
print("Tuple iteration")
t = ('I','am','in','tuple')
for i in t:
    print(i)

# iteration over a string
print("String iteration")
s = "Bandhan"
for i in s:
    print(i)

# iteration over a set
print("Set iteration")
num_set = {3,2,5,6,-2}
for i in num_set:
    print(i)

# dictionary iteration
print("Dictionary iteration")
d = {1:"Bandhan",2:"Singh",4:"katoch"}
for i in d:
    print(d[i])