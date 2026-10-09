import random
coin=random.choice(["heads", "tails"])
print(coin)
#or
from random import choice

coin = choice(["heads", "tails"])   # no "random." needed
print(coin)

#same functions
from random import choice
from my_tools import choice as my_choice

furniture = ["chair", "table", "sofa"]

print(choice(furniture))      
print(my_choice(furniture))  

#platform module
import platform

import platform

print("Operating system:", platform.system())
print("OS release:", platform.release())
print("Machine type:", platform.machine())
print("Processor:", platform.processor())
print("Python version:", platform.python_version())

#statistics
import statistics

data = [1, 2, 3, 4, 5]
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Standard deviation:", statistics.stdev(data))
print("Variance:", statistics.variance(data))