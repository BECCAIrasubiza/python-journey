readings1 = [22.5, 23.0, 21.8, 24.1, 22.9,
            23.4, 20.7, 21.5, 22.2, 23.1]

with open("readings1.txt", "w", encoding="utf-8") as file:
    for reading in readings1:
        file.write(f"{reading}\n")