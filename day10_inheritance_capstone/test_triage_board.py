
import csv
import pytest
from triage_board import Person, Patient, Nurse, load_patients, sort_by_triage, write_board


def test_from_record_good():
    p = Patient.from_record("Uwase, Diane | MRN10234 | 2\n")
    assert p.name == "Diane Uwase"        # flipped to First Last
    assert p.mrn == "MRN10234"
    assert p.triage == 2
    assert str(p) == "[2] Diane Uwase (MRN10234)"


def test_from_record_bad():
    with pytest.raises(ValueError):
        Patient.from_record("this line is broken")
    with pytest.raises(ValueError):
        Patient.from_record("Okafor, Ngozi | MRN1100 | 3")     # bad MRN
    with pytest.raises(ValueError):
        Patient.from_record("Brown, Tom | MRN11417 | 9")       # bad triage


def test_inheritance():
    # Patient and Nurse both reuse Person's name check
    with pytest.raises(ValueError):
        Patient("  ", "MRN10234", 2)
    with pytest.raises(ValueError):
        Nurse("", "ER")


def test_nurse_assign():
    nurse = Nurse("Grace", "Resuscitation")
    patient = Patient("John Smith", "MRN11005", 1)
    assert nurse.assign(patient) == "John Smith assigned to Nurse Grace (Resuscitation)"


def test_load_patients():
    patients, skipped = load_patients("admissions.txt")
    assert len(patients) == 6
    assert skipped == 3


def test_sort_by_triage():
    patients = [
        Patient("A", "MRN00001", 3),
        Patient("B", "MRN00002", 1),
        Patient("C", "MRN00003", 2),
    ]
    names = []
    for p in sort_by_triage(patients):
        names.append(p.name)
    assert names == ["B", "C", "A"]


def test_write_board():
    write_board("test_board.csv", [Patient("A", "MRN00001", 1)])
    rows = []
    with open("test_board.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    assert rows == [{"triage": "1", "name": "A", "mrn": "MRN00001", "urgent": "True"}]
