
import re


class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f"{self.hours}h {self.minutes}m"

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        hours = self.hours + other.hours + total_minutes // 60   # carry full hours
        minutes = total_minutes % 60                              # what's left over
        return Duration(hours, minutes)

    @classmethod
    def from_string(cls, text):
        if matches := re.fullmatch(r"(\d+)h (\d+)m", text.strip()):
            return cls(int(matches.group(1)), int(matches.group(2)))
        raise ValueError("Use the format 2h 15m")

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours):
        if hours < 0:
            raise ValueError("Hours can't be negative")
        self._hours = hours

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        if minutes < 0 or minutes > 59:
            raise ValueError("Minutes must be 0-59")
        self._minutes = minutes


def main():
    # Total time a patient spent in each stage of an ED visit
    triage = Duration.from_string("0h 25m")
    waiting = Duration.from_string("2h 50m")
    treatment = Duration.from_string("1h 40m")
    print("Total time in ED:", triage + waiting + treatment)


if __name__ == "__main__":
    main()
