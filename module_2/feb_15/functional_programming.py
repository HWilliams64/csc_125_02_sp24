def function_1(arg):
    print("function_1", arg)


def function_2(arg):
    print("function_2", arg)


def main(arg, function):
    function(arg)


word = "SOMETHING"

for i in range(10):
    main(i, function_1 if i < 5 else function_2)

    # Above is a ternary operation which is equivalent to the code below:
    # if i < 5:
    #     main(i, function_1)
    # else:
    #     main(i, function_2)


def black_box(x, y):
    pass