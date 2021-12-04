# program to list all the files in the folder or subfolder using os.walk() function
import os
path = "sample"
for root,dirs,files in os.walk(path):
    for file in files:
        print(os.path.join(root,file))

# for specific file extension
print()
print("For specific file :")
for root,dirs,files in os.walk(path):
    for file in files:
        if file.endswith(".py"):
            print(os.path.join(file))

