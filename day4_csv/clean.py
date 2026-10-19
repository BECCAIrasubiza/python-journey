"""Day 4 CHALLENGE – clean a messy admissions file.

Usage:  python clean.py admissions_raw.csv admissions_clean.csv

The raw file has real-world problems:
  * names stored as "Last, First" in ONE column (notice the quotes – the comma
    is INSIDE the name, which is exactly why we use the csv library)
  * a duplicated row
  * a row with a missing triage level

Your program must:
  1. split name into  first  and  last  columns
  2. drop duplicate rows
  3. skip rows with missing triage and report how many were skipped
  4. sort by triage (1 = most urgent) using sorted() + lambda
  5. write the result with csv.DictWriter
  6. exit cleanly (sys.exit) on wrong arguments or a missing input file
"""
import csv
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python clean.py INPUT.csv OUTPUT.csv")

    # ---- read ----
    rows = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    # ---- clean ----
    seen = []          # rows we have already kept, to spot duplicates
    cleaned = []
    skipped = 0
    for row in rows:
        if row in seen:                 # duplicate -> skip
            skipped += 1
            continue
        if row["triage"] == "":         # missing triage -> skip
            skipped += 1
            continue
        seen.append(row)
        last, first = row["name"].split(", ")    # "Uwase, Diane" -> "Uwase", "Diane"
        cleaned.append({
            "first": first,
            "last": last,
            "triage": int(row["triage"]),
            "arrival": row["arrival"],
        })

    # ---- sort ----  (patients with the same triage keep their original order)
    cleaned = sorted(cleaned, key=lambda r: r["triage"])

    # ---- write ----
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "triage", "arrival"])
        writer.writeheader()
        for row in cleaned:
            writer.writerow(row)

    print(f"Kept {len(cleaned)} rows, skipped {skipped} (missing triage or duplicate)")


if __name__ == "__main__":
    main()
