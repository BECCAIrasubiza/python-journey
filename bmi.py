def main():
    weight = float(input("Weight (kg): "))
    height = float(input("Height (m): "))
    value = bmi(weight, height)
    print(f"BMI: {value} -> {category(value)}")


def bmi(weight_kg, height_m):
    """Return BMI rounded to 1 decimal place."""
    return round(weight_kg / height_m**2, 1)


def category(value):
    """WHO adult categories."""
    if value < 18.5:
        return "Underweight"
    elif value < 25:
        return "Normal"
    elif value < 30:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    main()
