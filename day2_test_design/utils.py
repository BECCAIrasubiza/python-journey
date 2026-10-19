


def is_valid_age(n):
  
    if n < 0:
        raise ValueError("age cannot be negative")
    if n <= 120:
        return True
    else:
        return False


def convert_minutes(m):
   
    if m < 0:
        raise ValueError("minutes cannot be negative")
    hours = m // 60
    minutes = m % 60
    return f"{hours}h {minutes}m"


def classify(score):
    """Letter grade from a 0-100 score."""
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
