def main():
    x = int(input("what's x?"))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    if  n % 2 == 0: # even simpler terms return True if n % 2 == 0 else return False
        return True
    else:
        return False

main()