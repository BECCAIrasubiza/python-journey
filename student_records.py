FILENAME = "students.txt"


def ensure_file_exists():
    # "a" creates the file if it does not exist; no existing content is deleted.
    with open(FILENAME, "a", encoding="utf-8"):
        pass


def read_students():
    ensure_file_exists()
    students = []
    with open(FILENAME, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                name, course, score_text = parts
                try:
                    score = float(score_text)
                    students.append({"name": name, "course": course, "score": score})
                except ValueError:
                    print(f"Skipping record with invalid score: {line.strip()}")
    return students


def add_student():
    name = input("Student name: ").strip()
    course = input("Course: ").strip()
    if not name or not course or "," in name or "," in course:
        print("Name and course are required and cannot contain commas.")
        return

    try:
        score = float(input("Score (0-100): ").strip())
        if not 0 <= score <= 100:
            print("Score must be between 0 and 100.")
            return
    except ValueError:
        print("Score must be a number.")
        return

    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"{name},{course},{score:g}\n")
    print("Student added.")


def view_students():
    students = read_students()
    if not students:
        print("No student records yet.")
        return
    for student in students:
        print(f"{student['name']} | {student['course']} | {student['score']:g}")


def search_student():
    search_name = input("Name to search: ").strip().casefold()
    matches = [s for s in read_students() if search_name in s["name"].casefold()]
    if matches:
        for student in matches:
            print(f"{student['name']} | {student['course']} | {student['score']:g}")
    else:
        print("No matching student found.")


def show_statistics():
    students = read_students()
    if not students:
        print("No records to calculate statistics.")
        return

    scores = [s["score"] for s in students]
    print(f"Average score: {sum(scores) / len(scores):.2f}")
    highest = max(students, key=lambda s: s["score"])
    print(f"Highest scorer: {highest['name']} ({highest['score']:g})")

    course_counts = {}
    for student in students:
        course_counts[student["course"]] = course_counts.get(student["course"], 0) + 1
    print("Students per course:")
    for course, count in sorted(course_counts.items()):
        print(f"  {course}: {count}")


def delete_student():
    target = input("Exact name to delete: ").strip().casefold()
    students = read_students()
    kept = [s for s in students if s["name"].casefold() != target]
    removed_count = len(students) - len(kept)

    with open(FILENAME, "w", encoding="utf-8") as file:
        for student in kept:
            file.write(f"{student['name']},{student['course']},{student['score']:g}\n")

    print(f"Deleted {removed_count} record(s)." if removed_count else "No matching student found.")


def export_report():
    students = read_students()
    with open("report.txt", "w", encoding="utf-8") as report:
        report.write("STUDENT REPORT\n")
        report.write("==============\n")
        report.write(f"Number of students: {len(students)}\n")
        if students:
            scores = [s["score"] for s in students]
            report.write(f"Average score: {sum(scores) / len(scores):.2f}\n")
            highest = max(students, key=lambda s: s["score"])
            report.write(f"Highest scorer: {highest['name']} ({highest['score']:g})\n")
            report.write("\nSTUDENTS\n")
            for student in students:
                report.write(
                    f"{student['name']} | {student['course']} | {student['score']:g}\n"
                )
    print("Report saved to report.txt.")


def main():
    ensure_file_exists()
    while True:
        print("\nSTUDENT RECORDS")
        print("1. Add student")
        print("2. View all")
        print("3. Search by name")
        print("4. Statistics")
        print("5. Delete student")
        print("6. Export report")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            show_statistics()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            export_report()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Choose one of the listed options.")


if __name__ == "__main__":
    main()
