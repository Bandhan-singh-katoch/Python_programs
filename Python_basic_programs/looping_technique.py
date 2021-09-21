# ====================== Looping technique ===================
# https://www.geeksforgeeks.org/looping-techniques-python/?ref=lbp

# using enumerate()
for key, value in enumerate(['I','am','Bandhan','Singh']):
    print(key,value)

# using zip() : used to combine two similar containers ( list-list or dict-dict) printing the values sequentially.
questions = ['name', 'branch', 'college']
answers = ['Bandhan', 'btech', 'GGI']

for question, answer in zip(questions,answers):
    print("What is your {} ? {}".format(question,answer))    # What is your name ? Bandhan ......

# using items() to loop through the dictionary printing the dictionary key value-pair sequentially

d = {"a":"Bandhan", "b":"Singh", "c":"Katoch"}
for i,j in d.items():
    print(i,j)

# using sorted() : sorted() is used to print the container in sorted order. It doesn't sort the container
# but just prints the container in sorted order for 1 instance.

l = [2,1,7,4,8,3,1]
for a in sorted(l):
    print(a,end=" ")          # 1 1 2 3 4 7 8

# fo removing the similar elements we can use set.
print()
for a in sorted(set(l)):
    print(a,end=" ")           # 1 2 3 4 7 8

# reversed() : used to print the container in the reversed order. But no effect on the container.
print()
for i in reversed(range(1,10)):
    print(i,end=" ")             # 9 8 7 6 5 4 3 2 1





