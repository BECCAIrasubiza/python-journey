"""

BAD (hard to test):   def hello(to="world"): print("hello,", to)
   -> print() is a SIDE EFFECT. It returns None, so `assert hello() == ...` can't work.

GOOD (easy to test):  return the string, and let main() decide to print it.
"""


def main():
    name = input("What's your name? ")
    print(hello(name))


def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()
