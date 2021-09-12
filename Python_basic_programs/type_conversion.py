# python Type conversion and type casting

# implicit type conversion : in this type conversion python automatically converts one datatype to another datatype without any user involvement.
int_num = 2
flo_num = 3.5
new_num = flo_num + int_num
print(new_num)
print(type(new_num))
print(type(int_num))
print(type(flo_num))

# Explicit type conversion: In Explicit Type Conversion user convert the datatype of one object to another type.
# For that we use the predefined functions like int(), float(), str() etc. This type of conversion is also known as
# "typecasting" because in this the user casts(changes) the datatype of the object.
num_int = 3
num_str = "23"
num_str = int(num_str)   # After commenting this line it will show error
print(num_int+num_str)


