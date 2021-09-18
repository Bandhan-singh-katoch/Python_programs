# =============== Python if else statements ===================

# ---------------- if statement -----------------------
if(4%2 == 0):
    print("I am in if statement block")

print("I am not in if block")

# ---------------- if else statement ------------------
i= 5
if i>4:
    print("i am greater than 4")
else:
    print("i am lesser than 4")

# ---------------- nested if statement ------------------
if i>3:
    if i<9:
        print("i am greater than 2 and less than 9")
else: print("i am not greater than 2 and less than 9")

# ---------------- nested if statement ------------------
# we have i = 5
if i>5:
    print("I am greater than 5")
elif i == 5:
    print("I am equal to 5")
else:
    print("I am less than 5")

# ---------------- shorthand if statement ------------------
# shorthand if statement is used whenever we have only one statement in the if block. The statement can be put in the same line
if i<6: print("{} is less than 6".format(i))

# ---------------- shorthand if else statement ------------------
# This can be used to write if else statement in a single line, where there is only one statement in both the if and else block
a = 5
print("{} is greater than 4".format(a)) if a>4 else print("{} is less than 4".format(a))