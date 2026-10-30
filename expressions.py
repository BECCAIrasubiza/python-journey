import re
text=input("Enter a string: ")
if re.findall(r'\bRebecca\b', text, re.IGNORECASE):
    print("The name 'Rebecca' was found in the text.")
else:
    print("No occurrences of the name 'Rebecca' found in the text.")

import re

text = "My student ID is CS2026"

print(re.findall(r"\d", text))
print(re.findall(r"\w", text))
print(re.findall(r"\D", text))

import re

text = "I have 2 books, 15 pens, and 300 pages."

print(re.findall(r"\d*", text))

import re

pattern = r"3\.14"

print(bool(re.search(pattern, "3.14")))
print(bool(re.search(pattern, "3x14")))