from bmi import bmi, category


def test_bmi_value():
    assert bmi(70, 1.75) == 22.9
    assert bmi(50, 1.60) == 19.5


def test_category_middle_values():
    assert category(16.0) == "Underweight"
    assert category(22.0) == "Normal"
    assert category(27.0) == "Overweight"
    assert category(35.0) == "Obese"


def test_category_boundaries():
    # Exactly ON the cut-off belongs to the HIGHER category
    assert category(18.4) == "Underweight"
    assert category(18.5) == "Normal"
    assert category(24.9) == "Normal"
    assert category(25.0) == "Overweight"
    assert category(29.9) == "Overweight"
    assert category(30.0) == "Obese"
