import os

print("Current working directory is: " + os.getcwd())
my_path = os.path.join("/", "home", "developer")
print("My path exists", os.path.exists(my_path), 
"\nis a directory? ", os.path.isdir(my_path), 
"\nis a file? ", os.path.isfile(my_path))


