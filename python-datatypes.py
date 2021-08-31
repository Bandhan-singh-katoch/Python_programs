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
a = [2, 4.0, 5, 6, 33, 3.0, "string"]
print(a[2])
print(a[1:4])
print(a[3:])
# lists are mutable means the value of the element can be changed
a[1] = 44
print(a)

# tuples: same as list but are immutable means the value can't be changed
a = (5, 9.0, "bandhan")
print(a)
# a[0] = 6    # uncomment it, then it will show error

# strings
s = "i am string"
print(s)
s = """i am multi
line string"""
print(s)

# sets: unordered collection of unique elements
# sets are unordered collection of elements so indexing has no meaning
# and the slicing operator [] does not work
a = {1, 3, 2, 9, 4, 1}
print(a)


# dictionary: unordered collection of key:value pair
dict = {2:"Bandhan", 'key':"Singh"}
print(dict[2])
print(dict['key'])
