# ==================  pass statement ====================
# In python programming, the pass statement is a null statement. The difference between the
# comment and pass is that the comment is ignored by the interpreter but pass is not ignored
# We generally use it as a placeholder. eg: Like we have a loop or function and we don't know
# what to write in it but we want to implement it in future. Then we use pass. If we leave the block empty then it will show error.

# -------------------- pass in empty function -------------------
def vacant():
    pass

# -------------------- pass in empty class -------------------
class demo:
    pass

# -------------------- pass in for loop -------------------
for i in "Bandhan":
    pass

# -------------------- pass in conditional statement -------------------
a,b = 5,2
if a < 5:
    pass
else: print(b)