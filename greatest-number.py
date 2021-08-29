# greatest number among three numbers

n1 = float(input("Enter the first number :"))
n2 = float(input("Enter the second number :"))
n3 = float(input("Enter the third number :"))

# using if else elif statement
if (n1 > n2) and (n1 > n3):
    largest = n1
elif (n2 > n1) and (n2 > n3):
    largest = n2
else:
    largest = n3

print("The largest number is :", largest)
