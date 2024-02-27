# What is hashing?
# Hashing a process of converting data to unique ID
# - This ID should be unique
# - ID should evenly distributed 

my_string = "This is a string"
my_other_string = "This is another string"
number = 10000000

array = [None, None, None, None, None]

print("My string hash:", hash(my_string) % 4)
print("My other string hash:", hash(my_other_string) % 4)

array[hash(my_string) % 4] = my_string
array[hash(my_other_string) % 4] = my_other_string

print(array)

if array[hash(my_string) % 4] is not None:
    print("Has my string in the array")
