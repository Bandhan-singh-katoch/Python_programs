# program to read file character by character i.e. one character then nxt line...
# https://www.geeksforgeeks.org/python-program-to-read-character-by-character-from-a-file/
file = open("gfg.txt","r")
while 1:
    char = file.read(1)
    if not char:
        break
    print(char)
file.close()
