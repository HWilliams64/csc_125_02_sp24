def add(*x, y = " ", z = " "):
    print(f"x {x}, y {y}, z {z}")
    return sum(x)

# result = add("a", "b")
# print(result)

# result = add("a")
# print(result)


result = add(1,2,3,4,5,6,7,8,9,10, y=10)
print(result)
print("Hello", "how", "are", "you", sep="|")


def cat(*words, sep = ", "):
    return sep.join(words)

grocery_list = cat("apple", "banana", "cherry", "bread", "milk")
print(grocery_list)
