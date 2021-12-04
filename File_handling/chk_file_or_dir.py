# program to check if the path is file or directory
import os

path = 'samples'
if os.path.isfile(path):
    print("Given path is file")
if os.path.isdir(path):
    print("Given path is directory")
