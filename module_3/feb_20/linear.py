my_str = "Hello"
my_tup = ["H", "e", "l", "l", "o", 1, False, ()]

first_str = my_str[0]
first_elem = my_tup[0]

for elem in my_tup:
    print(elem, end="")

my_tup[0] = "Hello"
print()
print(my_tup)

# insert 
my_tup.insert(0, "1st")
print(my_tup)
# append
my_tup.append("last")
print(my_tup)
# extend
print("="*80)
a = []
b = []
a.extend([1, 2, 3])
b.append([1, 2, 3])
print(a)
print(b)

# remove
a = [5, 1, 5, 2, 3, 5, 4, 5, 6]
for _ in range(a.count(5)):
    a.remove(5)
    
while 5 in a:
    a.remove(5)

print(a)