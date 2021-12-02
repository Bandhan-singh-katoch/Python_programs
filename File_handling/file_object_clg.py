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