
import re


def main():
    print("Postal code:", is_postal_code(input("Postal code: ").strip()))
    print("Phone:", is_rwanda_phone(input("Phone: ").strip()))
    print("Student number:", is_student_number(input("Student number: ").strip()))


def is_postal_code(text):
    # [A-Z] = one capital letter,  [0-9] = one digit
    if re.search(r"^[A-Z][0-9][A-Z] [0-9][A-Z][0-9]$", text):
        return True
    return False


def is_rwanda_phone(text):
    # [2389] = exactly ONE of the characters 2, 3, 8 or 9
    # [0-9]{3} = exactly three digits
    if re.search(r"^\+250 7[2389][0-9] [0-9]{3} [0-9]{3}$", text):
        return True
    return False


def is_student_number(text):
    if re.search(r"^[0-9]{9}$", text):
        return True
    return False


if __name__ == "__main__":
    main()
