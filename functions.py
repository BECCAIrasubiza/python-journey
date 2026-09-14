def square():
    number=int(input("Enter a number:"))
    return number ** 2

result = square()
print("The square of the number is:", result) 


def is_even(n):
    
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
  
    if n % 2 != 0:
        return True
    else:
        return False
number=int(input("Enter a number:"))
print("Is the number even?", is_even(number))
print("Is the number odd?", is_odd(number))
def full_name(first, last):
    return first + " " + last
name= full_name("Rebecca", "Smith")
print("Full name:", name)