def check_password():
    password= input("set your password:")
    attempts=0
    max_attempts=10
    while attempts < max_attempts:
        p=input("enter a password: ")
        attempts +=1
        if p == password:
            print("success")
            print(attempts)
            return
        else:
            rm=max_attempts-attempts
            print("wrong password")
            if rm>0:
                print("you have", rm, "attempts left")
    print("you have used all your attempts")
    print("access denied")
check_password()    

def guess_number():
    secret_number=int(input("enter a secret number:"))
    guess=0
    max_guess=3
    while guess<max_guess:
        number=int(input("the secret number is:"))
        guess +=1
        if secret_number==number:
            print("the user got it")
            return
        else:
            remaining= max_guess-guess
            if remaining>0:
                print(f" you have {remaining} trials")
    print("out of guesses")
guess_number()

def sum_numbers():
    numbers = input("Enter numbers separated by spaces: ")
    numbers = numbers.split()

    total = 0

    for number in numbers:
        total += int(number)

    return total


result = sum_numbers()
print("The sum is:", result)

def sum_until_zero():
    total = 0

    number = int(input("Enter a number (0 to stop): "))

    while number != 0:
        total += number
        number = int(input("Enter a number (0 to stop): "))

    print("Total:", total)


sum_until_zero()

def greet_with_welcome(name, hometown):
    print("Greetings, I am", name, "living at", hometown)

name = input("What's your name? ")
hometown = input("What's your hometown? ")

greet_with_welcome(name, hometown)


    



                

    

    



