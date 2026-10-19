


class Student:
    def __init__(self, name, house):
        self.name = name       # save the argument inside THIS object
        self.house = house

    def greeting(self):
        return f"{self.name} from {self.house}"


def main():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)      # Python calls __init__ for us
    print(student.greeting())

    other = Student("Ron", "Gryffindor")
    print(other.greeting())             # each object keeps its OWN attributes


if __name__ == "__main__":
    main()
