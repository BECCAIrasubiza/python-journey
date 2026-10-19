
import csv
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python los.py INPUT.csv OUTPUT.csv")
    try:
        patients = load_patients(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    print("Top 3 longest stays:")
    for p in longest_stays(patients, 3):
        print(f"{p['name']}: {p['los']} hours ({p['department']})")

    averages = average_by_department(patients)
    write_summary(sys.argv[2], averages)
    print(f"Wrote {sys.argv[2]}")


def load_patients(path):
    """Read the CSV and return a list of dicts with los as an int."""
    patients = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            patients.append({
                "name": row["name"],
                "department": row["department"],
                "los": int(row["length_of_stay_hours"]),
            })
    return patients


def longest_stays(patients, n):
    """Return the n patients with the longest length of stay."""
    ordered = sorted(patients, key=lambda p: p["los"], reverse=True)
    return ordered[:n]          # [:n] = the first n items of the list


def average_by_department(patients):
    """Return a dict like {"Emergency": 5.8, "Cardiology": 56.5}."""
    stays = {}
    for p in patients:
        if p["department"] not in stays:
            stays[p["department"]] = []
        stays[p["department"]].append(p["los"])

    averages = {}
    for dept in sorted(stays):
        averages[dept] = round(sum(stays[dept]) / len(stays[dept]), 1)
    return averages


def write_summary(path, averages):
    with open(path, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["department", "average_los_hours"])
        writer.writeheader()
        for dept in averages:
            writer.writerow({"department": dept, "average_los_hours": averages[dept]})


if __name__ == "__main__":
    main()
