from formats import is_postal_code, is_rwanda_phone, is_student_number


def test_postal_good():
    assert is_postal_code("V5A 1S6") == True
    assert is_postal_code("V3T 0A3") == True


def test_postal_bad():
    assert is_postal_code("v5a 1s6") == False     # lowercase
    assert is_postal_code("V5A1S6") == False      # missing space
    assert is_postal_code("55A 1S6") == False     # digit where a letter goes
    assert is_postal_code("V5A 1S6X") == False    # extra character ($ catches it)


def test_phone_good():
    assert is_rwanda_phone("+250 788 123 456") == True
    assert is_rwanda_phone("+250 722 000 999") == True


def test_phone_bad():
    assert is_rwanda_phone("250 788 123 456") == False    # no +
    assert is_rwanda_phone("+250 768 123 456") == False   # 6 not allowed after 7
    assert is_rwanda_phone("+250 788 12 3456") == False   # wrong grouping
    assert is_rwanda_phone("+250 788 123 4567") == False  # too many digits


def test_student_number():
    assert is_student_number("301234567") == True
    assert is_student_number("30123456") == False     # 8 digits
    assert is_student_number("3012345678") == False   # 10 digits
    assert is_student_number("30123456a") == False    # letter
