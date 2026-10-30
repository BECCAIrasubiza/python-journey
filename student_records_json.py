import json

FILENAME = "students.json"


def load_students():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("The JSON file is invalid; starting with an empty list.")
        return []


def save_students(students):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=2)


def main():
    students = load_students()
    name = input("Student name: ").strip()
    course = input("Course: ").strip()

    try:
        score = float(input("Score (0-100): ").strip())
        if not 0 <= score <= 100:
            raise ValueError
    except ValueError:
        print("Enter a number from 0 to 100.")
        return

    students.append({"name": name, "course": course, "score": score})
    save_students(students)
    print(f"Saved {len(students)} student record(s) to {FILENAME}.")


if __name__ == "__main__":
    main()
