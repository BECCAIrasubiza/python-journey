# a list using break statement
from os import remove


x=["apple","banana","cherry"]
for i in x:
    if i=="banana":
        break
    print(i)
#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#turning the split string into integer
a = "1,2,3,4"
b = a.split(",")
b = list(map(int, b))

print(b)

#finding the median of a list
a = input("Enter a list of numbers separated by commas: ")
b = list(map(int, a.split(",")))

b.sort()

n = len(b)

if n % 2 == 1:
    median = b[n // 2]
else:
    median = (b[n // 2 - 1] + b[n // 2]) / 2

print(median)

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#list initialization
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#inserting an item in a list
thislist = ["apple", "banana", "cherry"]
thislist[1]="blackcurrant"
thislist.insert(2, "watermelon")
print(thislist)

#append is used to add an item to the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)

#checking for items in a list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#exercise
colors = ["red", "green", "blue", "yellow"]
print(colors[0])  # Output: red
colors[1] = "orange"
colors.append("violet")
remove(colors[0])
print(colors)  


