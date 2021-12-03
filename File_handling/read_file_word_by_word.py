# program to read file word by word
file = open("gfg.txt","r")
for line in file:
    for word in line.split():
        print(word)
file.close()