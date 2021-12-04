# program to count number of characters in a file
file = open("geek.txt")
data = file.read()
print(len(data))
file.close()

# count characters excluding spaces
file = open("geek.txt")
data = file.read().replace(" ","")
print(len(data))
file.close()