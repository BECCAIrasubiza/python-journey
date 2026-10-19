
import csv
import re
import sys


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name.strip():
            raise ValueError("Missing name")
        self._name = name.strip()


class Patient(Person):
    def __init__(self, name, mrn, triage):
        super().__init__(name)
        self.mrn = mrn
        self.triage = triage

    def __str__(self):
        return f"[{self.triage}] {self.name} ({self.mrn})"

    def is_urgent(self):
        return self.triage <= 2

    @classmethod
    def from_record(cls, line):
        """Build a Patient from text like  'Uwase, Diane | MRN10234 | 2'."""
        pattern = r"(.+), *(.+) \| (\S+) \| (\d+)"
        if matches := re.fullmatch(pattern, line.strip()):
            name = matches.group(2) + " " + matches.group(1)    # First Last
            return cls(name, matches.group(3), int(matches.group(4)))
        raise ValueError("Record is not in the right format")

    @property
    def mrn(self):
        return self._mrn

    @mrn.setter
    def mrn(self, mrn):
        if not re.fullmatch(r"MRN\d{5}", mrn):
            raise ValueError("Invalid MRN")
        self._mrn = mrn

    @property
    def triage(self):
        return self._triage

    @triage.setter
    def triage(self, triage):
        if triage not in [1, 2, 3, 4, 5]:
            raise ValueError("Triage must be 1-5")
        self._triage = triage


class Nurse(Person):
    def __init__(self, name, ward):
        super().__init__(name)
        self.ward = ward

    def __str__(self):
        return f"Nurse {self.name} ({self.ward})"

    def assign(self, patient):
        return f"{patient.name} assigned to {self}"


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python triage_board.py ADMISSIONS.txt OUTPUT.csv")

    patients, skipped = load_patients(sys.argv[1])
    board = sort_by_triage(patients)

    print("=== TRIAGE BOARD ===")
    for patient in board:
        print(patient)

    nurse = Nurse("Grace", "Resuscitation")
    print("\n=== URGENT ASSIGNMENTS ===")
    for patient in board:
        if patient.is_urgent():
            print(nurse.assign(patient))

    write_board(sys.argv[2], board)
    print(f"\n{len(board)} patients saved to {sys.argv[2]}, {skipped} records skipped")


def load_patients(path):
    """Return (list of Patients, number of bad lines)."""
    patients = []
    skipped = 0
    try:
        with open(path) as file:
            for line in file:
                try:
                    patients.append(Patient.from_record(line))
                except ValueError:
                    skipped += 1
    except FileNotFoundError:
        sys.exit(f"Could not read {path}")
    return patients, skipped


def sort_by_triage(patients):
    return sorted(patients, key=lambda p: p.triage)


def write_board(path, patients):
    with open(path, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["triage", "name", "mrn", "urgent"])
        writer.writeheader()
        for p in patients:
            writer.writerow({"triage": p.triage, "name": p.name, "mrn": p.mrn, "urgent": p.is_urgent()})


if __name__ == "__main__":
    main()
