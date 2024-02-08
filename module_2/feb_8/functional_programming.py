def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def convert_and_cal(user_input, calc_func):
    values = user_input.split()

    total = 0
    for value in values:
        total = calc_func(total, int(value))

    return total

user_input = input("Enter your numbers: ")

total_add = convert_and_cal(user_input, add)

total_sub = convert_and_cal(user_input, sub)

total_div = convert_and_cal(user_input, div)

print(total_add, total_sub, total_div)
