
import re


def main():
    email = input("What's your email? ").strip()
    if is_valid(email):
        print("Valid")
    else:
        print("Invalid")


def is_valid(email):
    # re.fullmatch already checks from the start to the end, so ^ and $ aren't needed
    if re.fullmatch(r"(\w|\.)+@(\w+\.)?\w+\.(edu|com|org|ca)", email, re.IGNORECASE):
        return True
    return False


if __name__ == "__main__":
    main()
