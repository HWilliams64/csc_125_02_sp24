import hashlib

saved_password_hash = '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b'

password = hashlib.sha256(input("Please type your password: ").encode('utf-8')).hexdigest()

print(f"Correct password:{saved_password_hash == password}")
