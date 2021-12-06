import re
str = "GeeksforGeeks: A computer science portal for geeks"
match = re.search(r'portal',str)
print("Start index = ",match.start())
print("End index = ",match.end())