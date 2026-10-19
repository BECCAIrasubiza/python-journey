def calculate_mean(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    return mean

def calculate_median(numbers):
  numbers = sorted(numbers)
  n = len(numbers)
  if n % 2 == 1:
    median = numbers[n // 2]
  else:
    middle1 = numbers[n // 2 - 1]
    middle2 = numbers[n // 2]
    median = (middle1 + middle2) / 2

    return median

numbers = input("Enter numbers: ").split();

valid_numbers = [int(num) for num in numbers]

print(valid_numbers)
# mean = calculate_mean(numbers)
# median = calculate_median(numbers)
# print("value of mean:", mean)
# print("value of median:", median)

 

    






