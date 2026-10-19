#sending list as an argument
def my_function(children):
    for child in children:
        print(child)
my_children=["Joan","Jess","Jessan","Jovan"]
my_function(my_children)

#sending dictionary as an argument
def my_beloved(loves):
    print(f"my beloved names: {loves['name']} and their age is: {loves['age']}")

my_loves = {
    "name": ["Micah", "Levi"],
    "age": [1, 4]
}
my_beloved(my_loves)

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

numbers = input("Enter numbers: ").split()

numbers = [int(num) for num in numbers]

result = my_function(*numbers)

print("Total:", result)

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))