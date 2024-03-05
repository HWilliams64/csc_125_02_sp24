student = {
    "first_name": "Tony",
    "last_name" : "Stark",
    "id": 3000,
    "dob": "5/29/70",
    "grades":[]
}

# Access a single value
#print(student["first_name"])

# Modify a value
student["first_name"] = "Carol"
student["last_name"] = "Danvers"

#print(student["first_name"])

# Add a value
student["address"] = "Boston MA"
#print(student)

# Remove
# Check if middle name is in the student before deleting
if "middle_name" in student:
    del student["middle_name"]

# Remove a key/value and return it's value default to None
student['nickname'] = "Captian Marval"
nickname = student.pop("nickname", None)
#print("The removed nickname:", nickname)
# Undo
student['nickname'] = nickname

#print(student)

# Loop over all the keys
# for key in student:
#     print(key, ":", student[key])

for key, value in student.items():
    print(f"{key}:{value}")
