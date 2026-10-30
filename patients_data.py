class Patient:
    def __init__(self, name, age, heart_rate):
        self.name = name
        self.age = age
        self.heart_rate = heart_rate


patient1 = Patient("Becca", 23, 75)
patient2 = Patient("John", 30, 82)

print(patient1.name)
print(patient2.name)
print(patient1.heart_rate)
print(patient2.heart_rate)