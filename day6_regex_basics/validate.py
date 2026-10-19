
import re


def main():
    email = input("What's your email? ").strip()
    if is_valid(email):
        print("Valid")
    else:
        print("Invalid")


def is_valid(email):
    if re.search(r"^[^@ ]+@[^@ ]+\.edu$", email):
        return True
    return False


if __name__ == "__main__":
    main()
