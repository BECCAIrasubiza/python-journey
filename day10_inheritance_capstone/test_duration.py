
import pytest
from duration import Duration


def test_str():
    assert str(Duration(2, 15)) == "2h 15m"
    assert str(Duration(0, 5)) == "0h 5m"


def test_add_simple():
    assert str(Duration(1, 10) + Duration(2, 20)) == "3h 30m"


def test_add_carries_minutes():
    assert str(Duration(1, 50) + Duration(0, 20)) == "2h 10m"
    assert str(Duration(0, 59) + Duration(0, 1)) == "1h 0m"


def test_add_three():
    total = Duration(0, 25) + Duration(2, 50) + Duration(1, 40)
    assert str(total) == "4h 55m"


def test_from_string():
    d = Duration.from_string("2h 15m")
    assert d.hours == 2
    assert d.minutes == 15


def test_from_string_bad_format():
    with pytest.raises(ValueError):
        Duration.from_string("2 hours 15 minutes")
    with pytest.raises(ValueError):
        Duration.from_string("2h15m")


def test_invalid_values():
    with pytest.raises(ValueError):
        Duration(1, 60)
    with pytest.raises(ValueError):
        Duration(-1, 0)
    with pytest.raises(ValueError):
        Duration.from_string("1h 75m")     # regex passes, but the setter catches it
