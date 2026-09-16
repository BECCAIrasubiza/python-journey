x=int(input("What's x? "))
y=int(input("what's y?"))
if x<y:
    print("x is less than y")
if x>y:
    print("x is greater than y")
if x==y:
    print("x is equal to y")


age=int(input("Age:"))
if age>=65:
    print("You need retirement planning")
elif age>=18:
    print("You are an adult")
else:
    print("You are a minor")

# logic operators: and/or/not

a=int(input("What's a? "))
b=int(input("what's b?"))

if a < b and b > a:
    print("a is not equal to b")
else:
    print("a is equal to b")


temp= int(input("what's the temperature? "))
if temp > 20 and temp < 30:
    print("Comfortable")      # and — both must be true

if temp < 0 or temp > 35:
    print("Extreme")          # or — at least one true

if not (temp > 30):
    print("Not hot")          # not — flips the result


