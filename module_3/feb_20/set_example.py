# Use case
# - Order does not matter
# - Frequently checking existence

# - You cannot use the access operator `[]`

my_set1 = {"h", "e", "l", "l", "o"}
my_set2 = {"l", "h", "o", "e",  "l"}
print(my_set1)
print(my_set2)

# adding values to our set
my_set1.add("a")
print(my_set1)

my_set1.update(["a", "b", "c"])  # similar to the extends in the list
print(my_set1)

# remove a value from our set
if "a" in my_set1:
    my_set1.remove("a")
    print(my_set1)

# Check if a value exists in our set

# check if set 1 a sub set of set 2
print(my_set2.issubset(['e', 'o', 'h', 'l', 'a', 'b', 'c']))
print(my_set1.isdisjoint([1, 2, 3, 4, 5, 6]))
print(my_set1.intersection([1, 2, 3, 4, 5, 6, "a", "b", "c"]))
print(my_set1.difference([1, 2, 3, 4, 5, 6, "a", "b", "c"]))

print("="*80)
print(my_set1)
for value in my_set1:
    print(value)