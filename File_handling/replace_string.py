# program to replace string in file
fin = open("read.txt","r")
fout = open("read1.txt","w")
for i in fin:
    fout.write(i.replace('bandan','Bandhan'))
fin.close()
fout.close()