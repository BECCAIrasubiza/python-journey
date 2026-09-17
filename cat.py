i=0
while  i<10: 
    print ("meow")
    i=i+1

for i in range(10): # use this instead of making a list 
    print("Love")
print("love\n" * 10, end="")

#n=int(input("What's n? "))
i#f n < 0:
  #  n=int(input("what's n? "))

while True:
    n=int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

    # example
for letter in "banana":
    print(letter)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # enumerate is used for identifyong the position
students={
    "Alice": 3,
    "Bob": 5,
    "Charlie": 7

}

for student in students:
    print(student, students[student], sep=": ")
for index, student in enumerate(students):
    print(index, student, students[student], sep=": ")