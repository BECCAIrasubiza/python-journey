try:
    students = []
    with open("scores.txt", "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                name, score_text = line.split(",")
                score = float(score_text.strip())
                students.append((name.strip(), score))
            except ValueError:
                print(f"Skipping malformed line {line_number}: {line}")

    if not students:
        print("No valid scores found.")
    else:
        scores = [score for name, score in students]
        sorted_scores = sorted(scores)
        count = len(sorted_scores)
        middle = count // 2

        if count % 2 == 1:
            median = sorted_scores[middle]
        else:
            median = (sorted_scores[middle - 1] + sorted_scores[middle]) / 2

        mean = sum(scores) / count
        top_three = sorted(students, key=lambda student: student[1], reverse=True)[:3]

        bands = {
            "0-49": sum(1 for score in scores if 0 <= score < 50),
            "50-69": sum(1 for score in scores if 50 <= score < 70),
            "70-100": sum(1 for score in scores if 70 <= score <= 100),
        }

        report_lines = [
            "STUDENT SCORE REPORT\n",
            "====================\n",
            f"Number of students: {count}\n",
            f"Minimum score: {min(scores):.2f}\n",
            f"Maximum score: {max(scores):.2f}\n",
            f"Mean score: {mean:.2f}\n",
            f"Median score: {median:.2f}\n",
            "\nTOP 3 STUDENTS\n",
            "--------------\n",
        ]
        for rank, (name, score) in enumerate(top_three, start=1):
            report_lines.append(f"{rank}. {name}: {score:g}\n")

        report_lines.extend([
            "\nSCORE BANDS\n",
            "-----------\n",
            f"0-49: {bands['0-49']}\n",
            f"50-69: {bands['50-69']}\n",
            f"70-100: {bands['70-100']}\n",
        ])

        with open("stats_report.txt", "w", encoding="utf-8") as report:
            report.writelines(report_lines)

        print("Report saved to stats_report.txt")
        print(f"Mean: {mean:.2f}; median: {median:.2f}")

        # Optional check using Python's statistics module.
        import statistics
        print(f"statistics.mean check: {statistics.mean(scores):.2f}")
        print(f"statistics.median check: {statistics.median(scores):.2f}")

except FileNotFoundError:
    print("Sorry, scores.txt was not found.")
