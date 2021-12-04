# Program to replace multiple spaces with single space in a Text File

with open("geek.txt") as fin:
    data = fin.read().split()
    data = " ".join(data)

with open("geek.txt","w") as fout:
    fout.write(data)
