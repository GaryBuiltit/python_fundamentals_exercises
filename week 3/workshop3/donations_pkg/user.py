
def login(database, username, password):
    if username in database and password == database[username]:
        print(f"welcome to DonateMe {username}")
        return username
    elif username in database and password != database[username]:
        print("Incorrect Password")
        return ""
    else:
        print("User not found. Please register or check you records")
        return ""


def register(database, username, password):
    if username in database:
        print("Username already registered")
        return ""
    elif len(username) > 10:
        print("Username can be a maximum of 10 characters")
        return ""
    elif len(password) < 5:
        print("Password must be atleast 5 characters")
        return ""
    else:
        print(f"User {username} registered")
        return username
