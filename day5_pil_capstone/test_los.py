"""Day 5 CAPSTONE tests – Lecture 5 testing applied to Lecture 6 file code.

Run:  pytest test_los.py -v
"""
import csv
import pytest
from los import load_patients, longest_stays, average_by_department, write_summary

SAMPLE = [
    {"name": "A", "department": "ER", "los": 4},
    {"name": "B", "department": "ER", "los": 6},
    {"name": "C", "department": "Cardio", "los": 50},
]


def test_longest_stays_order():
    top = longest_stays(SAMPLE, 2)
    assert top[0]["name"] == "C"
    assert top[1]["name"] == "B"
    assert len(top) == 2


def test_longest_stays_n_bigger_than_list():
    assert len(longest_stays(SAMPLE, 10)) == 3


def test_average_by_department():
    assert average_by_department(SAMPLE) == {"Cardio": 50.0, "ER": 5.0}


def test_average_empty():
    assert average_by_department([]) == {}


def test_load_patients():
    # test_patients.csv is a tiny CSV file made just for this test
    patients = load_patients("test_patients.csv")
    assert len(patients) == 2
    assert patients[0] == {"name": "Z", "department": "ER", "los": 7}


def test_load_missing_file():
    with pytest.raises(FileNotFoundError):
        load_patients("does_not_exist.csv")


def test_write_then_read_back():
    write_summary("test_output.csv", {"ER": 5.0})
    rows = []
    with open("test_output.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    # remember: everything read from a CSV comes back as a string
    assert rows == [{"department": "ER", "average_los_hours": "5.0"}]
