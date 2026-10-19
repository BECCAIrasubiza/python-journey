
import pytest
from ed_patient import Patient


def test_valid_patient():
    p = Patient("Diane Uwase", "MRN10234", 2)
    assert str(p) == "Diane Uwase (MRN10234) - triage 2"


def test_name_is_stripped():
    assert Patient("  Eric  ", "MRN10871", 4).name == "Eric"


def test_bad_name():
    with pytest.raises(ValueError):
        Patient("", "MRN10234", 2)
    with pytest.raises(ValueError):
        Patient("   ", "MRN10234", 2)


def test_bad_mrn():
    with pytest.raises(ValueError):
        Patient("Eric", "MRN1023", 2)      # 4 digits
    with pytest.raises(ValueError):
        Patient("Eric", "MRN102345", 2)    # 6 digits
    with pytest.raises(ValueError):
        Patient("Eric", "mrn10234", 2)     # lowercase
    with pytest.raises(ValueError):
        Patient("Eric", "10234", 2)        # no MRN


def test_bad_triage():
    with pytest.raises(ValueError):
        Patient("Eric", "MRN10234", 0)
    with pytest.raises(ValueError):
        Patient("Eric", "MRN10234", 6)


def test_setter_after_creation():
    p = Patient("Eric", "MRN10234", 3)
    with pytest.raises(ValueError):
        p.triage = 9
    assert p.triage == 3


def test_is_urgent():
    assert Patient("A", "MRN00001", 1).is_urgent() == True
    assert Patient("A", "MRN00001", 2).is_urgent() == True
    assert Patient("A", "MRN00001", 3).is_urgent() == False


def test_escalate():
    p = Patient("A", "MRN00001", 3)
    p.escalate()
    assert p.triage == 2
    p.escalate()
    assert p.triage == 1
    with pytest.raises(ValueError):
        p.escalate()
