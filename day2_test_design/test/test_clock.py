import pytest
from clock import convert


def test_morning():
    assert convert("9:00 AM") == "09:00"
    assert convert("11:59 AM") == "11:59"


def test_afternoon():
    assert convert("1:05 PM") == "13:05"
    assert convert("11:59 PM") == "23:59"


def test_midnight_and_noon():
    assert convert("12:00 AM") == "00:00"
    assert convert("12:15 AM") == "00:15"
    assert convert("12:00 PM") == "12:00"


def test_extra_spaces_at_ends_are_ok():
    assert convert("  7:45 PM ") == "19:45"


def test_hour_out_of_range():
    with pytest.raises(ValueError):
        convert("13:00 PM")
    with pytest.raises(ValueError):
        convert("0:30 AM")


def test_minute_out_of_range():
    with pytest.raises(ValueError):
        convert("9:60 AM")
    with pytest.raises(ValueError):
        convert("9:5 AM")


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9:00")          # missing AM/PM
    with pytest.raises(ValueError):
        convert("9:00 am")       # lowercase
    with pytest.raises(ValueError):
        convert("9 AM")          # missing minutes
    with pytest.raises(ValueError):
        convert("cat")           # nonsense
