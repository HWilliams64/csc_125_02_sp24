password = "password123"
user_input = input("Please enter your password: ")

same_password = user_input == password

# if same_password:
#     print("Password is the same!")
# else:
#     print("Password is not the same!")
#     if len(user_input) < len(password):
#         print("The password you typed in is too short!")
#     elif len(user_input) > len(password):
#         print("The password you typed in is too long!")
#     else:
#         print("The password you typed in is not the same!")

if same_password:
    print("Password is the same!")
elif not user_input.startswith(password[0]):
    print("The password you typed in does not start with the correct character!")
elif len(user_input) < len(password):
    print("The password you typed in is too short!")
elif len(user_input) > len(password):
    print("The password you typed in is too long!")
else:
    print("Password is not the same!")
