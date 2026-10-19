
from patient import Patient, load_patients, count_long_stays


def test_attributes():
    p = Patient("Amina", "Emergency", 6)
    assert p.name == "Amina"
    assert p.department == "Emergency"
    assert p.los_hours == 6


def test_los_days():
    assert Patient("A", "ER", 48).los_days() == 2.0
    assert Patient("A", "ER", 30).los_days() == 1.2


def test_is_long_stay_boundary():
    assert Patient("A", "ER", 23).is_long_stay() == False
    assert Patient("A", "ER", 24).is_long_stay() == True       # exactly 24 counts
    assert Patient("A", "ER", 10).is_long_stay(threshold=8) == True


def test_summary():
    assert Patient("Brian", "Cardiology", 52).summary() == "Brian (Cardiology): 52 h = 2.2 days"


def test_load_patients():
    patients = load_patients("patients.csv")
    assert len(patients) == 15
    assert patients[0].name == "Amina"
    assert patients[0].los_hours == 6      # converted to int, not "6"


def test_count_long_stays():
    patients = [
        Patient("A", "ER", 5),
        Patient("B", "Cardio", 50),
        Patient("C", "Cardio", 30),
    ]
    assert count_long_stays(patients) == {"ER": 0, "Cardio": 2}
