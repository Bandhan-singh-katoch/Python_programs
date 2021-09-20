# Loop control statement: Loop control statements change the execution from the normal sequence.

# ----------------- Continue statement ---------------------
# continue statement is used to skip the rest of the code for the current iteration only. Loop does not terminate
# but continues with the next iteration.

for letter in "Bandhan Singh":
    if letter == 'n':     # if letter == a then it will skip rest of the code and continue with the next iteration
        continue
    print(letter)
print("\n")
# ----------------- Break statement ------------------------
# break statement is used to terminate the loop containing it. Control of the program flows to the statement immediately after the loop

for letter in "Bandhan":
    if letter == 'd':
        break
    print(letter)

# ----------------- Pass statement -------------------------
# pass statement is used to write the empty loops, functions, classes.
for alpha in "alphabets":
    pass                                   # pass is used whenever we don't have anything to write.
                                           # If we leave the block blank then it will show error
print("Last element of alpha is = ",alpha)

# ----------------- range() constructor or method -------------------------
print()
# printing a number
for i in range(10):
    print(i,end=" ")

# using for iteration
print()
l = [90,12,35,63]
for i in range(len(l)):
    print(l[i],end=" ")

# sum of first 5 numbers
print()
s=0
for i in range(1,5):
    s += i
print("Sum = ",s)


# ------------------- for loop with else -------------------
# the else statement just after the loop is executed only if there is no break statement.
for i in range(1,4):
    print(i)
else: print("No break")    # executed as there is no break

for i in range(6,9):
    print(i)
    break
else:print("with break")      # Not executed as we have break





