import hashlib

db = {
    "ironman": {
        "first_name": "Tony",
        "last_name": "Stark",
        "id": 3000,
        "dob": "5/29/70",
        "password": "4f278cdddf52263fe21c64c94932f2b2ec316acecd39a7adcc01eb2e6592a678"
    },
    "captain_m": {
        "first_name": "Carol",
        "last_name": "Danvers",
        "id": 4000,
        "dob": "5/29/70",
        "password": "ce6ef27cad6153acfe2bc469e65dd9d3aacb201086f6ac43a458cea9429f8a3a"
    },
}

while True:

    username = input("Please type your username:")

    user = db.get(username, {})

    password = input("Please type your password:")
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    saved_password_hash = user.get("password")

    if not saved_password_hash or password_hash != saved_password_hash:
        print("Username and password do not match")
    else:
        print(f"Welcome to shield {user['first_name']}")