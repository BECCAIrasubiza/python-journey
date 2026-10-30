

import re

def is_valid_username():
    username = input("Enter all usernames separated by commas: ")

    usernames = [u.strip() for u in username.split(",")]

    valid_usernames = []
    invalid_usernames = []

    for u in usernames:
        if re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{2,15}", u):
            valid_usernames.append(u)
            print(f"{u}: Valid")
        else:
            invalid_usernames.append(u)
            print(f"{u}: Invalid")

    count_valid_usernames = len(valid_usernames)
    count_invalid_usernames = len(invalid_usernames)

    valid_usernames_percentage = (
        count_valid_usernames / len(usernames)
    ) * 100

    print("\n--- Summary ---")
    print(f"Valid usernames: {count_valid_usernames}")
    print(f"Invalid usernames: {count_invalid_usernames}")
    print(f"Percentage of valid usernames: {valid_usernames_percentage:.2f}%")

    print(f"List of valid usernames: {valid_usernames}")
    print(f"List of invalid usernames: {invalid_usernames}")

is_valid_username()
