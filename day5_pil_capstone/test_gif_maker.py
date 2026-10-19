import pytest
from gif_maker import check_files, valid_speed


def test_speed_valid():
    assert valid_speed("50") == True
    assert valid_speed("300") == True
    assert valid_speed("2000") == True


def test_speed_out_of_range():
    assert valid_speed("49") == False
    assert valid_speed("2001") == False
    assert valid_speed("-100") == False


def test_speed_not_a_number():
    assert valid_speed("fast") == False
    assert valid_speed("1.5") == False
    assert valid_speed("") == False


def test_files_ok():
    # returns nothing and does NOT exit when everything is fine
    check_files(["a.gif", "b.png", "c.jpg"])


def test_too_few_files():
    with pytest.raises(SystemExit):
        check_files(["a.gif"])
    with pytest.raises(SystemExit):
        check_files([])


def test_wrong_extension():
    with pytest.raises(SystemExit):
        check_files(["a.gif", "notes.txt"])
