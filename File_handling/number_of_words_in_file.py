# Program to count number of words in the text file
file = open("geek.txt")
data = file.read()
print(len(data.split()))
file.close()