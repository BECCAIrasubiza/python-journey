


class Student:
    def __init__(self, name, house, patronus=None):
        self.name = name          # these lines call the SETTERS below
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        if self.patronus == "Stag":
            return "🐴"
        elif self.patronus == "Otter":
            return "🦦"
        elif self.patronus == "Jack Russell terrier":
            return "🐶"
        else:
            return "🪄"

    # ----- name: getter and setter -----
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # ----- house: getter and setter -----
    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)                       # uses __str__
    print("Expecto Patronum!", student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
