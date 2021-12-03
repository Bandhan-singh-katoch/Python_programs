import os

# program to create the directory or folder
os.mkdir("sample")
print("Folder created")

# creating directory after verifying if the directory already exist
if not os.path.isdir("samples"):
    os.mkdir("samples")
else:
    print("This directory already exists")
