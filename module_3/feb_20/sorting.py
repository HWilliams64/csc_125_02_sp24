import random

my_list = [1, 2, 3, 4, 5, 6, "a", "b", "c", "1", "2", "3", "4", "5"]

#my_list = list(random.sample(range(1, 100), 10))

def key(value):
    if isinstance(value, str):
        return value
    else:
        return "z"+str(value)

print(my_list)
my_list.sort(key=key)
print(my_list)
