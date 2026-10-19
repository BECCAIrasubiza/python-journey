def main():
    print_column(3)
    print_row(4)
    print_square(5)

def print_column(height):
    for _ in range(height):
        print("#\n" * height, end="")

def print_row(width):
    print("?" * width)


def print_square(size):
    #for each row in square
    for i in range(size):
        #for each column in square
        for j in range(size):
            #print brick
            print("#", end="")
    
        print()

    for i in range(size):
        print_row(size)
def print_row(width):


    print("#" * width)
main()