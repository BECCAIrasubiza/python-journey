readings = [22.5, 23.0, 21.8, 24.1, 22.9, 23.4, 20.7, 21.5, 22.2, 23.1]

# Start fresh each run: "w" replaces the previous file.
with open("readings.txt", "w", encoding="utf-8") as file:
    for reading in readings:
        file.write(f"{reading}\n")

# Append exactly 3 extra readings.
extra_readings = [24.0, 22.7, 21.9]
with open("readings.txt", "a", encoding="utf-8") as file:
    for reading in extra_readings:
        file.write(f"{reading}\n")

# readline(): first line
with open("readings.txt", "r", encoding="utf-8") as file:
    first_line = file.readline().strip()
print(f"First reading: {first_line}")

# readlines(): list of all lines; last item is the last line
with open("readings.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
print(f"Last reading: {lines[-1].strip()}")

# Count lines with a for loop, and calculate the average.
total = 0.0
count = 0
with open("readings.txt", "r", encoding="utf-8") as file:
    for line in file:
        temperature = float(line.strip())
        total += temperature
        count += 1

average = total / count if count else 0
print(f"Total lines: {count}")
print(f"Average temperature: {average:.2f}")
print("Expected: 13 lines")
