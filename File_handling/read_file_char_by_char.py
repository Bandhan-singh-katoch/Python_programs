# program to read file character by character i.e. one character then nxt line...
file = open("gfg.txt","r")
while 1:
    char = file.read(1)
    if not char:
        break
    print(char)
file.close()
