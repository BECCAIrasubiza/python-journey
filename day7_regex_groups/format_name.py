
import re


def main():
    name = input("What's your name? ").strip()
    print(f"hello, {format_name(name)}")


def format_name(name):
    #                  (last)  comma, any spaces   (first)
    if matches := re.search(r"^(.+), *(.+)$", name):
        name = matches.group(2) + " " + matches.group(1)
    return name


if __name__ == "__main__":
    main()
