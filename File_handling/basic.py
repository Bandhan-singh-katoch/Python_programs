file = open("geek.txt","r")
for i in file:
    print(i)

# Output: I am bandhan singh from jammu

# Working of read() mode
f = open("geek.txt","r")
print(f.read())
# Output: I am bandhan singh from jammu

f = open("geek.txt","r")
print(f.read(4))
# Output: I am