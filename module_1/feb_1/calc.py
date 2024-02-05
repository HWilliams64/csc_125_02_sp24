run = True
while run:

    num_str_1 = input("Please type a number:")

    if not num_str_1.isdigit():
        print(f"'{num_str_1}' is not a digit")
        continue # restart the loop from here
    
    operation = input("Please type a operation (+, -, *, /):")

    if operation not in "+-*/":
        print(f"'{operation}' is not a valid operation")
        continue  # restart the loop from here

    num_str_2 = input("Please type a number:")

    if not num_str_2.isdigit():
        print(f"'{num_str_2}' is not a digit")
        continue

    # Step 1 - convert the string into numbers
    num_1 = float(num_str_1)
    num_2 = float(num_str_2)
    
    # Step 2 - catagroize the operation
    if operation == "+":
        # Step 3 - calculate the value
        print(f"{num_1} {operation} {num_2} = {num_1 + num_2}")
    elif operation == "-":
        # Step 3 - calculate the value
        print(f"{num_1} {operation} {num_2} = {num_1 - num_2}")
    elif operation == "*":
        # Step 3 - calculate the value
        print(f"{num_1} {operation} {num_2} = {num_1 * num_2}")
    elif operation == "/":
        # Step 3 - calculate the value
        print(f"{num_1} {operation} {num_2} = {num_1 / num_2}")

    keep_going = input("Would you like to continue? (y/n):")
    if keep_going.lower() == "n":
        run = False 
        break # This stops the loop
