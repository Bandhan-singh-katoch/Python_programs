#  ========================= while loop =========================

count = 0
while count < 4:
    count = count+1
    print(count,end=" ")          # 1 2 3 4

print()
# -------------------------- python while loop with list -----------------
l = [34,2,8,44]
while l:
    print(l.pop(), end=" ")          # 44 8 2 34

print()

# ------------------------- single statement while loop ----------------
count = 0
while count < 4: count+=1; print(count, end=" ")       # 1 2 3 4  similar to 1st program at the top