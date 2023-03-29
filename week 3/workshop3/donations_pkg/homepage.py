
def show_homepage():
    print("""
        === DonateME Homepage ===
----------------------------------------
| 1.    Login     | 2.  Register        |
----------------------------------------
| 3.    Donate    | 4.  Show Donations  |
----------------------------------------
|               5. Exit                 |
----------------------------------------
    """)


def donate(username):
    try:
        donation_amount = float(input("enter donation amount: "))
    except ValueError:
        print("Please input a number")
        return ""
    if donation_amount < 1 or type(donation_amount) == "string":
        print("Please input a number greater than 0")
        return ""
    else:
        donation_string = f"{username} doanted ${donation_amount}"
        print(f"Thank you for your donation {username}")
        donations = {donation_string: donation_amount}
    return donations


def show_donations(donations, total_donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("There is no donations yet.")
    else:
        for donation in donations:
            print(donation)
    print(f"Total = ${total_donations}")
