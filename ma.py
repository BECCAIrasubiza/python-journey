import math
numbers = input("Enter numbers separated by commas: ")
numbers = list(map(int, numbers.split(",")))

mean = sum(numbers) / len(numbers)

squared_differences = []


for x in numbers:
    difference = x - mean
    squared = difference ** 2
    squared_differences.append(squared)
    variance = sum(squared_differences) / len(squared_differences)
    standard_deviation = math.sqrt(variance)

print("Mean:", mean)
print("Variance:", variance)
print("Standard deviation:", standard_deviation)


