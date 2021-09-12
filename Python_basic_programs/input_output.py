# I am writing only that code that i don't know
# Output

print(1,2,3,4)                  # 1 2 3 4
print(1,2,3,4,sep='*')          # 1*2*3*4
print(1,2,3,4,sep='*',end='$')  # 1*2*3*4$
print("\n")

# output formatting i.e. str.format() , this method is used to make the output more attractive.
print("Hlo {} I am {}".format("Bandhan","Bikesh"))
print("Hlo {0} I am {1}".format("Bandhan","Bikesh"))
print("Hlo {1} I am {0}".format("Bandhan","Bikesh"))
print("Good morning {name}, where is section {section}".format(section='A',name='Ayush'))

# Input: Syntax is input([prompt]) where prompt is the string that we want to display on screen
num = input('Enter the number = ')
print(num)         # 14
print(type(num))   # <class 'str'> : Here the number entered in the form of string so we use int(), float() to convert into number
print(int(num)+int(num))