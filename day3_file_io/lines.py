
import sys


def main():
    filename = check_arguments(sys.argv)
    try:
        with open(filename) as file:
            print(count_lines(file))
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_arguments(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")
    if not argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    return argv[1]


def count_lines(lines):
    """Works on an open file OR a plain list of strings -> easy to test."""
    count = 0
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            count += 1
    return count


if __name__ == "__main__":
    main()
