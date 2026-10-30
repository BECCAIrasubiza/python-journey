try:
    with open("dirty_ages.txt", "r", encoding="utf-8") as source:
        with open("clean_ages.txt", "w", encoding="utf-8") as clean_file, \
             open("rejected.txt", "w", encoding="utf-8") as rejected_file:
            good_count = 0
            rejected_count = 0
            total_count = 0

            for line_number, line in enumerate(source, start=1):
                total_count += 1
                raw_value = line.strip()

                try:
                    age = int(raw_value)
                    if 0 <= age <= 120:
                        clean_file.write(f"{age}\n")
                        good_count += 1
                    else:
                        rejected_file.write(f"line {line_number}: {raw_value}\n")
                        rejected_count += 1
                except ValueError:
                    rejected_file.write(f"line {line_number}: {raw_value}\n")
                    rejected_count += 1

    rejected_percentage = (rejected_count / total_count * 100) if total_count else 0
    print(f"Valid ages: {good_count}")
    print(f"Rejected lines: {rejected_count}")
    print(f"Percentage rejected: {rejected_percentage:.2f}%")

except FileNotFoundError:
    print("Sorry, dirty_ages.txt was not found. Put it in the same folder as this script.")
