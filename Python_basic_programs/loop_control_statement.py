# Loop control statement: Loop control statements change the execution from the normal sequence.

# ----------------- Continue statement ---------------------
# continue statement is used to skip the rest of the code for the current iteration only. Loop does not terminate
# but continues with the next iteration.

for letter in "Bandhan Singh":
    if letter == 'n':     # if letter == a then it will skip rest of the code and continue with the next iteration
        continue
    print(letter)