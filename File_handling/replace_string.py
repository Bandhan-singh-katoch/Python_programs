# program to replace string in file
fin = open("read.txt","r")
fout = open("read1.txt","w")
for i in fin:
    fout.write(i.replace('bandan','Bandhan'))
fin.close()
fout.close()


print()

# ---------- replacing string in the same file -------------
fin = open("read.txt","r")
data = fin.read()
data = data.replace("Jammu","Ramban")
fin.close()

fout = open("read.txt","w")
fout.write(data)
fout.close()