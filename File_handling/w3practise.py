import os

file = open("w3file.txt","a")
file.write("THis is just for testing purpose\nAnd the content is from the w3schools website")
file.close()

file = open("w3file.txt","r")
print(file.readline())
print(file.readline())    # writing the readline() twice prints the second line also
file.close()

# --------- deleting of file ----------
os.remove("w3file.txt")