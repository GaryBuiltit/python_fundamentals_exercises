from donations_pkg.homepage import *
from donations_pkg.user import login, register


database = {"admin": "password123"}
donations = []
donations_total = 0
authorized_user = ""

while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user.capitalize()}")

    choice = input("Choose an option: ")
    print("")
    if choice == "1":
        username = input("Username: ").lower()
        password = input("Password: ")
        authorized_user = login(database, username, password)
        continue
    elif choice == "2":
        username = input("Choose a username: ").lower()
        password = input("Create your password: ")
        authorized_user = register(database, username, password)
        if authorized_user != "":
            database[username] = password
        authorized_user = ""
        continue
    elif choice == "3":
        if authorized_user == "":
            print("You are not logged in. Please login to make a donation")
        else:
            donation_returned = donate(authorized_user)
            if donation_returned != "":
                for donation_string, donation_amount in donation_returned.items():
                    donations.append(donation_string)
                    donations_total += donation_amount
        continue
    elif choice == "4":
        show_donations(donations, donations_total)
        continue
    elif choice == "5":
        print("Logging Out... Goodbye!")
        break
    else:
        print("Not a valid choice.")
