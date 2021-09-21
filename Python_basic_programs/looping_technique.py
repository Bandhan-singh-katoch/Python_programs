# ====================== Looping technique ===================
# https://www.geeksforgeeks.org/looping-techniques-python/?ref=lbp

# using enumerate()
for key, value in enumerate(['I','am','Bandhan','Singh']):
    print(key,value)

# using zip() : used to combine two similar containers ( list-list or dict-dict) printing the values sequentially.
questions = ['name', 'branch', 'college']
answers = ['Bandhan', 'btech', 'GGI']

for question, answer in zip(questions,answers):
    print("What is your {} ? {}".format(question,answer))


