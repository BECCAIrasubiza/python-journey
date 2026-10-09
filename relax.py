#lists
#1
groceries = ["milk", "bread", "eggs"]
groceries.append("butter")
groceries.insert(1,"apple")
groceries.remove("eggs")
print(groceries)
#2
numbers=[3,8,1,6,10,4,7]

newlist=[x for x in numbers if x%2==0 ]
print([x**2 for x in newlist])
#3
def sum_matrix(matrix):
    total = 0
    for row in matrix:
        total += sum(row)
    return total
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])
print(sum_matrix(matrix))

#4
def remove_duplicates(nums):
    return list(set(nums))
print(remove_duplicates([4, 2, 4, 5, 2, 9, 8, 1, 9]))

#tuples
#1
a=5
b=10
a,b=b,a
print(a,b)

#2
point = (3, 4)
mylist=list(point)
mylist[0]=5
point=tuple(mylist)
print(point)

#3
def min_max_avg(numbers):
    minimum=min(numbers)
    maximum=max(numbers)
    average=sum(numbers)/len(numbers)
    return minimum, maximum, average
numbers=list(map(int,input("Enter numbers separated by spaces: ").split()))
print(min_max_avg(numbers))

#set
visitors = ["Ada", "Sam", "Ada", "Kofi", "Sam", "Ada"]
unique_visitors = set(visitors)
print(unique_visitors)

#2
alice_friends = {"Sam", "Kofi", "Maya", "Jin"}
ben_friends = {"Kofi", "Jin", "Priya", "Noah"}
mutual_friends = alice_friends & ben_friends
different = alice_friends - ben_friends
friend_union = alice_friends | ben_friends
print(mutual_friends)
print(different)
print(friend_union)

#3
# a huge list of 10,000usernames
#4
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
symmetric_difference=set_a^set_b
print(symmetric_difference)

#dictionaries
scores = {"Ada": 92, "Sam": 85, "Kofi": 78}
scores["Maya"] = 95
scores["Sam"] = 90
#prints each student's name and score, one per line, using a loop
print("student scores:")
for student, score in scores.items():
    print(f"{student}: {score}")
#4
def total_value(inventory):
    total = 0
    for item in inventory.values():
        total += item["price"] * item["quantity"]
    return total

inventory = {
    "apple": {"price": 0.5, "quantity": 100},
    "banana": {"price": 0.3, "quantity": 150}
}

print(total_value(inventory))

data = [("Ada", 92), ("Sam", 85), ("Kofi", 78)]
data = [("Ada", 92), ("Sam", 85), ("Kofi", 78)]

result = {}

for name, score in data:
    result[name] = score

print(result)

numbers = [5, 2, 8, 1, 3]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers)