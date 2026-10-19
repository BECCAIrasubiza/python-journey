


def main():
    # ---- 1. TUPLE ----
    name, house = get_student_tuple()     # "unpacking" the tuple into two variables
    print(f"[tuple] {name} from {house}")

    student = get_student_tuple()
    print(f"[tuple] {student[0]} from {student[1]}")   # or use index 0 and 1

    # Tuples are IMMUTABLE (can't be changed). This would crash:
    #     student[1] = "Ravenclaw"   -> TypeError
    try:
        student[1] = "Ravenclaw"
    except TypeError:
        print("[tuple] can't change a tuple -> TypeError")

    # ---- 2. DICT ----
    student = get_student_dict()
    print(f"[dict]  {student['name']} from {student['house']}")
    student["house"] = "Ravenclaw"        # dicts CAN be changed
    print(f"[dict]  changed: {student['name']} from {student['house']}")


def get_student_tuple():
    name = "Harry"
    house = "Gryffindor"
    return name, house          # the comma makes a tuple: ("Harry", "Gryffindor")


def get_student_dict():
    return {"name": "Hermione", "house": "Gryffindor"}


if __name__ == "__main__":
    main()
