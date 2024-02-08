
def input_number(prompt):
    str_number = input(prompt)

    # while not str_number.isdigit():
    #     print(f"The value {str_number} is not a number.")
    #     str_number = input(prompt)
    if not str_number.isdigit():
        return input_number(f"The value {str_number} is not a number.\n{prompt}")

    number = float(str_number)
    return number

num1 = input_number("Enter a number: ")
num2 = input_number("Enter another number: ")
print(num1+ num2)
