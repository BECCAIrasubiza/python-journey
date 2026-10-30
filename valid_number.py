import re

phone = input("Enter your phone number: ")

if re.fullmatch(r"\d{10}", phone):
    print("Valid format")
else:
    print("Invalid format")
