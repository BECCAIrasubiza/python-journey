"""Tests grouped by CATEGORY of input – the main idea of Lecture 5, part 2."""
import pytest
from utils import is_valid_age, convert_minutes, classify



def test_age_normal():
    assert is_valid_age(30) == True
    assert is_valid_age(120) == True


def test_age_edges():
    assert is_valid_age(0) == True
    assert is_valid_age(121) == False


def test_age_negative():
    with pytest.raises(ValueError):
        is_valid_age(-1)



def test_minutes_positive():
    assert convert_minutes(135) == "2h 15m"
    assert convert_minutes(60) == "1h 0m"
    assert convert_minutes(45) == "0h 45m"


def test_minutes_zero():
    assert convert_minutes(0) == "0h 0m"


def test_minutes_negative():
    with pytest.raises(ValueError):
        convert_minutes(-5)


# ---------- classify ----------
def test_grades_each_letter():
    assert classify(95) == "A"
    assert classify(85) == "B"
    assert classify(75) == "C"
    assert classify(65) == "D"
    assert classify(10) == "F"


def test_grades_boundaries():
    assert classify(90) == "A"
    assert classify(89) == "B"
    assert classify(60) == "D"
    assert classify(59) == "F"
    assert classify(0) == "F"
    assert classify(100) == "A"


def test_grades_out_of_range():
    with pytest.raises(ValueError):
        classify(101)
    with pytest.raises(ValueError):
        classify(-1)
