# -------------- reading from a file ----------------
# read() : returns the read bytes in form of a string. reads n bytes, if no n specifiedd reads the entire file
file = open("read.txt","r")
print(file.read())

# readline() : reads a line of the file and returns in the form of string
file = open("read.txt","r")
print(file.readline())

# readlines() : reads all the lines and return them as each line a string element in a list
file = open("read.txt","r")
print(file.readlines())

