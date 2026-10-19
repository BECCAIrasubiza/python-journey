"""Day 2 CHALLENGE – convert 12-hour clock times to 24-hour time.

    convert("9:00 AM")   -> "09:00"
    convert("12:30 PM")  -> "12:30"
    convert("12:15 AM")  -> "00:15"
    convert("13:00 PM")  -> raises ValueError

Why it's challenging: midnight and noon are tricky edge cases, and
EVERY bad input must raise ValueError. Your tests must prove all of that.
"""


def main():
    print(convert(input("Time (e.g. 9:30 PM): ")))


def convert(s):
    # Step 1: split "9:30 PM" into "9:30" and "PM"
    try:
        time, period = s.strip().split(" ")
    except ValueError:
        # happens if there isn't exactly ONE space (e.g. "9:30" or "9 : 30 PM")
        raise ValueError("format must be H:MM AM/PM")

    if period != "AM" and period != "PM":
        raise ValueError("must end with AM or PM")

    # Step 2: split "9:30" into "9" and "30"
    try:
        hour, minute = time.split(":")
    except ValueError:
        raise ValueError("time must contain one colon")

    if len(minute) != 2:
        raise ValueError("minutes need two digits")

    # Step 3: turn text into numbers (int() raises ValueError on "ab")
    hour = int(hour)
    minute = int(minute)

    if hour < 1 or hour > 12:
        raise ValueError("hour must be 1-12")
    if minute < 0 or minute > 59:
        raise ValueError("minute must be 0-59")

    # Step 4: the actual conversion
    if period == "AM":
        if hour == 12:        # 12 AM is midnight -> 00
            hour = 0
    else:
        if hour != 12:        # 12 PM is noon -> stays 12
            hour = hour + 12

    # :02 pads with a zero, so 9 becomes 09
    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
