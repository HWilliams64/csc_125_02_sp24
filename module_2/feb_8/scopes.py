x = 20

def my_function():
    global x # <- DO NOT DO THIS

    x = x + 40
    print("Function called")
    print(x)
    return x


print(x) # 20
my_function()
print(x)  # 10, 20 and 10
