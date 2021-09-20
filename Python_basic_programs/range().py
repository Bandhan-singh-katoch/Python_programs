# ==================== range() =======================
# Basic program is in loop_control_statement.py file

#  SYNTAX =  range() constructor can be defined in two ways : range(stop) , range(start, stop, step)
for i in range(10):
    print(i,end=" ")              # 0 1 2 3 4 5 6 7 8 9

print()

for i in range(1,10,2):
    print(i,end=" ")          # 1 3 5 7 9

# --------------------- creating list by range() constructor -------------
print()
l = list(range(10))
print(l)

# ---------------------- creating list of even numbers using range() ------------
start = 2
stop = 10
step = 2
print(list(range(start,stop,step)))





