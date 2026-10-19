

def main():
    email = input("What's your email? ").strip()
    if is_valid(email):
        print("Valid")
    else:
        print("Invalid")


def is_valid(email):
    # split("@") breaks the text at each @ sign:
    # "malan@harvard.edu" -> ["malan", "harvard.edu"]
    parts = email.split("@")
    if len(parts) != 2:
        return False
    username = parts[0]
    domain = parts[1]
    if username and domain.endswith(".edu"):
        return True
    return False


if __name__ == "__main__":
    main()
