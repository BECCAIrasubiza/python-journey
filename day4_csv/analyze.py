
import csv

# 1. READ – DictReader uses the header row, so each row is a dict:
#    {"name": "Amina", "department": "Emergency", "length_of_stay_hours": "6"}
#    Every value arrives as a STRING, so we convert the number with int().
patients = []
with open("patients.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        patients.append({
            "name": row["name"],
            "department": row["department"],
            "los": int(row["length_of_stay_hours"]),
        })

# 2. SORT – key tells sorted() WHAT to compare.
#    lambda patient: patient["los"]  is a tiny unnamed function: "give me the los".
print("Longest stays first:")
for p in sorted(patients, key=lambda patient: patient["los"], reverse=True):
    print(f"{p['name']} ({p['department']}): {p['los']} hours")

# 3. GROUP – a dict where each department maps to a LIST of its stays
#    e.g. {"Emergency": [6, 4, 9, 3, 7], "Cardiology": [52, 71, 40, 63], ...}
stays = {}
for p in patients:
    if p["department"] not in stays:
        stays[p["department"]] = []
    stays[p["department"]].append(p["los"])

# 4. WRITE – DictWriter needs the column names (fieldnames) up front.
with open("summary.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["department", "patients", "average_los_hours"])
    writer.writeheader()
    for dept in sorted(stays):
        writer.writerow({
            "department": dept,
            "patients": len(stays[dept]),
            "average_los_hours": round(sum(stays[dept]) / len(stays[dept]), 1),
        })

print("\nWrote summary.csv")
