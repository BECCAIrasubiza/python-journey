
import re


class Patient:
    def __init__(self, name, mrn, triage):
        self.name = name
        self.mrn = mrn
        self.triage = triage

    def __str__(self):
        return f"{self.name} ({self.mrn}) - triage {self.triage}"

    def is_urgent(self):
        return self.triage <= 2

    def escalate(self):
        if self.triage == 1:
            raise ValueError("Already at the most urgent level")
        self.triage = self.triage - 1      # goes through the setter again

    # ----- name -----
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name.strip():
            raise ValueError("Missing name")
        self._name = name.strip()

    # ----- mrn -----
    @property
    def mrn(self):
        return self._mrn

    @mrn.setter
    def mrn(self, mrn):
        if not re.fullmatch(r"MRN\d{5}", mrn):
            raise ValueError("MRN must be MRN followed by 5 digits")
        self._mrn = mrn

    # ----- triage -----
    @property
    def triage(self):
        return self._triage

    @triage.setter
    def triage(self, triage):
        if triage not in [1, 2, 3, 4, 5]:
            raise ValueError("Triage must be 1-5")
        self._triage = triage


def main():
    try:
        name = input("Name: ")
        mrn = input("MRN: ")
        triage = int(input("Triage (1-5): "))
        patient = Patient(name, mrn, triage)
    except ValueError:
        print("Could not register patient: check the name, MRN and triage")
        return

    print(patient)
    if patient.is_urgent():
        print("URGENT - see immediately")


if __name__ == "__main__":
    main()
