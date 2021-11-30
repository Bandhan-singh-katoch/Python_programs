file = open("geek.txt","r")
for i in file:
    print(i)

# Output: I am bandhan singh from jammu

# --------------Working of read() mode ----------------------
f = open("geek.txt","r")
print(f.read())
# Output: I am bandhan singh from jammu

f = open("geek.txt","r")
print(f.read(4))
# Output: I am

# ------------creating a file using write() mode -----------------
file = open("geeks.txt","w")
file.write("I am in write mode")
file.close()

file = open("geeks.txt",'r')
print(file.read())

# Output: I am in write mode

# --------- working of append() mode ---------------------
f = open("geeks.txt","a")
f.write(" and i am geeks.txt wala file")

f = open("geeks.txt","r")
print(f.read())
