# in this file i will be practising the programs that are in mams ppt
#tell() : it returns an integer that tells us the file object/file handle position from the begining of the file in the form of bytes.
file = open("read.txt","r")
lines = file.read(10)
print(lines)
print(file.tell())
file.close()

# seek() : it is used to change the position of the file handle to give the specific position
#syntax : f.seek(offset,from_what)
print("seek() starts here")
f = open("read.txt","r")
f.seek(10)
print(f.tell())
print(f.readline())
f.close()

#flush() : flush() method clears the internal buffer of the file. close() automatically
# flushes the data but if u want to flush it before then it is used
print("flush() starts here :")
fileObj = open("read.txt","r")
fileObj.flush()
print(fileObj.read())
fileObj.close()

# another program of flush()
print("Another program of flush:- ")
file1 = open("gfg.txt","w")
file1.write("i am gfg.txt file")
file1.close()

file1 = open("gfg.txt","r")
fileContent = file1.read()
print("Content before flush:\n",fileContent)
file1.flush()
fileContent = file1.read()
print("Content after flush:\n",fileContent)
file1.close()

# ------------ file object attribute -------------
print("Attributes :- ")
file2 = open("read.txt","r")
print("File name = ",file2.name)
print("File mode = ",file2.mode)
print("File closed = ",file2.closed)
print("Content in file :\n",file2.read())
file2.close()
print("File closed = ",file2.closed)
