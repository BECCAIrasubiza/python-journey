r"""Day 2 CHALLENGE – parse a hospital Emergency Department log file.

Usage:  python log_parser.py ed_log.txt events.csv

Each good line looks like:
    2026-10-19 08:15 | ADMIT | MRN10234 | triage 2

Your program must:
  1. read the log file line by line                        (Week 1 – files)
  2. use ONE regex with capturing groups to pull out:
        date, time, event, mrn, triage
  3. accept the event in any case (admit / ADMIT)          (re.IGNORECASE)
  4. only accept events ADMIT, TRANSFER or DISCHARGE        (A|B|C)
  5. MRN must be "MRN" + exactly 5 digits, triage 1-5      (\d{5}, [1-5])
  6. count and report lines that don't match
  7. write the good lines to a CSV with csv.DictWriter     (Week 1 – CSV)
  8. print a privacy-safe version of each line where the MRN is hidden,
     e.g. MRN10234 -> MRN***34                              (re.sub)
"""
import csv
import re
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python log_parser.py LOG.txt OUTPUT.csv")

    events = []
    bad_lines = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                event = parse_line(line)
                if event == None:
                    bad_lines += 1
                else:
                    events.append(event)
                    print(mask_mrn(line.strip()))
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "time", "event", "mrn", "triage"])
        writer.writeheader()
        for event in events:
            writer.writerow(event)

    print(f"\n{len(events)} events saved to {sys.argv[2]}, {bad_lines} lines skipped")


def parse_line(line):
    """Return a dict for a good line, or None for a bad one."""
    pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) \| (ADMIT|TRANSFER|DISCHARGE) \| (MRN\d{5}) \| triage ([1-5])"
    if matches := re.fullmatch(pattern, line.strip(), re.IGNORECASE):
        return {
            "date": matches.group(1),
            "time": matches.group(2),
            "event": matches.group(3).upper(),
            "mrn": matches.group(4),
            "triage": int(matches.group(5)),
        }
    return None


def mask_mrn(text):
    """Hide the first 3 digits of every MRN:  MRN10234 -> MRN***34"""
    return re.sub(r"MRN\d{3}", "MRN***", text)


if __name__ == "__main__":
    main()
