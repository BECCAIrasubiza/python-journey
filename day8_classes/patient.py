
import csv


class Patient:
    def __init__(self, name, department, los_hours):
        self.name = name
        self.department = department
        self.los_hours = los_hours

    def los_days(self):
        return round(self.los_hours / 24, 1)

    def is_long_stay(self, threshold=24):
        return self.los_hours >= threshold

    def summary(self):
        return f"{self.name} ({self.department}): {self.los_hours} h = {self.los_days()} days"


def main():
    patients = load_patients("patients.csv")
    print("Long stays (24 h or more):")
    for p in patients:
        if p.is_long_stay():
            print("  " + p.summary())

    print("\nLong stays per department:")
    counts = count_long_stays(patients)
    for dept in counts:
        print(f"  {dept}: {counts[dept]}")


def load_patients(path):
    patients = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            patients.append(Patient(row["name"], row["department"], int(row["length_of_stay_hours"])))
    return patients


def count_long_stays(patients):
    counts = {}
    for p in patients:
        if p.department not in counts:
            counts[p.department] = 0
        if p.is_long_stay():
            counts[p.department] += 1
    return counts


if __name__ == "__main__":
    main()
