import sys
import statistics

if len(sys.argv) != 2:
    sys.exit("Usage: python analyze.py <data_file>")

with open(sys.argv[1], "r") as f:
    data = [float(line.strip()) for line in f]

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))



import sys
import statistics

# Make sure the user provided numbers
if len(sys.argv) < 2:
    print("Usage: python analyze.py number1 number2 number3 ...")
    sys.exit(1)

try:
    # Convert command-line arguments into numbers.
    # sys.argv[0] is the script name, so we skip it.
    data = [float(value) for value in sys.argv[1:]]

except ValueError:
    print("Error: Please provide only numeric values.")
    sys.exit(1)

# Calculate descriptive statistics
print("\nDATA SUMMARY")
print("-" * 30)
print("Data:", data)
print("Number of observations:", len(data))
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Minimum:", min(data))
print("Maximum:", max(data))
print("Population variance:", statistics.pvariance(data))
print("Population standard deviation:", statistics.pstdev(data))

# Sample statistics require at least two observations.
if len(data) >= 2:
    print("Sample variance:", statistics.variance(data))
    print("Sample standard deviation:", statistics.stdev(data))