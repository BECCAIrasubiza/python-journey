

FILENAME = "names.txt"


def main():
    add_names()
    names = read_names()
    print("\nA -> Z:")
    for name in sorted(names):
        print(f"  hello, {name}")
    print("\nZ -> A:")
    for name in sorted(names, reverse=True):
        print(f"  hello, {name}")


def add_names():
    
    with open(FILENAME, "a") as file:
        while True:
            name = input("Name (Enter to stop): ").strip()
            if not name:
                break
            file.write(f"{name}\n")


def read_names():
    
    names = []
    try:
        with open(FILENAME) as file:          # "r" (read) is the default mode
            for line in file:
                if line.strip():               # skip empty lines
                    names.append(line.rstrip())
    except FileNotFoundError:
        pass                                   # no file yet -> empty list
    return names


if __name__ == "__main__":
    main()
