
import pytest
from student import Student


def test_str():
    assert str(Student("Harry", "Gryffindor")) == "Harry from Gryffindor"


def test_charm():
    assert Student("Harry", "Gryffindor", "Stag").charm() == "🐴"
    assert Student("Hermione", "Gryffindor", "Otter").charm() == "🦦"
    assert Student("Padma", "Ravenclaw").charm() == "🪄"


def test_invalid_when_created():
    with pytest.raises(ValueError):
        Student("", "Gryffindor")
    with pytest.raises(ValueError):
        Student("Harry", "Number Four, Privet Drive")


def test_invalid_after_created():
    # The setter protects the object even AFTER it was made
    student = Student("Harry", "Gryffindor")
    with pytest.raises(ValueError):
        student.house = "Number Four, Privet Drive"
    assert student.house == "Gryffindor"        # unchanged


def test_valid_change():
    student = Student("Harry", "Gryffindor")
    student.house = "Slytherin"
    assert student.house == "Slytherin"
