# python data-types
# python numbers
a = 6
print(a, " is of type", type(a))

a = 6.0
print(a, " is of type", type(a))

a = 6+2j
print(a, " is of type", type(a))

# isinstance() function is used to check if an object belongs to a particular class.
print(a, "is complex number: ", isinstance(a, complex))


# python list: same as array but can be of different type
a = [2, 4, 5, 6, 33, 3, 8]
print(a[2])
print(a[1:4])
print(a[3:])
# lists are mutable means the value of the element can be changed
a[1] = 44
print(a)

# tuples:

