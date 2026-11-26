def get_grade_and_point(score):
    """Converts a numeric score (0-100) into a letter grade and grade point."""
    if 70 <= score <= 100:
        return "A", 5
    elif 60 <= score <= 69:
        return "B", 4
    elif 50 <= score <= 59:
        return "C", 3
    elif 45 <= score <= 49:
        return "D", 2
    elif 40 <= score <= 44:
        return "E", 1
    else:
        return "F", 0


def get_degree_class(cgpa):
    """Determines the Nigerian university class of degree on a 5.0 scale."""
    if cgpa >= 4.50:
        return "First Class Honours"
    elif cgpa >= 3.50:
        return "Second Class Honours (Upper Division)"
    elif cgpa >= 2.40:
        return "Second Class Honours (Lower Division)"
    elif cgpa >= 1.50:
        return "Third Class Honours"
    elif cgpa >= 1.00:
        return "Pass"
    else:
        return "Fail / Academic Probation"


def get_valid_int(prompt, min_val=None, max_val=None):
    """Safely gets an integer within an optional range without crashing."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Error: Value must be at least {min_val}. Try again.")
                continue
            if max_val is not None and value > max_val:
                print(f"Error: Value cannot exceed {max_val}. Try again.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")


def get_valid_float(prompt, min_val=0.0, max_val=None):
    """Safely gets a floating-point number within a range without crashing."""
    while True:
        try:
            value = float(input(prompt))
            if value < min_val:
                print(f"Error: Value cannot be less than {min_val}. Try again.")
                continue
            if max_val is not None and value > max_val:
                print(f"Error: Value cannot exceed {max_val}. Try again.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def collect_courses(num_courses):
    """Collects details for all courses and computes semester totals."""
    courses = []
    total_units = 0
    total_points = 0

    for i in range(1, num_courses + 1):
        print(f"\n--- Course {i} ---")
        while True:
            code = input("Enter Course Code (e.g., CSC 101): ").strip().upper()
            if code:
                break
            print("Error: Course code cannot be empty.")

        unit = get_valid_int("Enter Credit Unit (e.g., 3): ", min_val=1, max_val=20)
        score = get_valid_float("Enter Score (0 - 100): ", min_val=0.0, max_val=100.0)

        grade, point = get_grade_and_point(score)
        weighted_point = unit * point

        total_units += unit
        total_points += weighted_point

        courses.append({
            "code": code,
            "unit": unit,
            "score": score,
            "grade": grade,
            "point": point,
            "weighted_point": weighted_point
        })

    return courses, total_units, total_points


def calculate_cgpa(sem_units, sem_points):
    """Calculates CGPA by optionally including previous semester records."""
    while True:
        has_prev = input("\nDo you have previous semester records to include for CGPA? (y/n): ").strip().lower()
        if has_prev in ("y", "yes"):
            prev_units = get_valid_int("Enter total previous Credit Units: ", min_val=1)
            prev_cgpa = get_valid_float("Enter previous CGPA (0.00 - 5.00): ", min_val=0.0, max_val=5.0)
            prev_points = prev_units * prev_cgpa

            cum_units = prev_units + sem_units
            cum_points = prev_points + sem_points
            return round(cum_points / cum_units, 2), cum_units, round(cum_points, 2)
        elif has_prev in ("n", "no"):
            return round(sem_points / sem_units, 2), sem_units, sem_points
        else:
            print("Error: Please enter 'y' or 'n'.")


def format_report(name, department, courses, sem_units, sem_points, gpa, cgpa, degree_class):
    """Formats the academic summary as a clean text report."""
    lines = [
        "=" * 60,
        "              UNIVERSITY GPA & CGPA RESULT SLIP",
        "=" * 60,
        f"Student Name : {name}",
        f"Department   : {department}",
        "-" * 60,
        f"{'Course Code':<15}{'Unit':<8}{'Score':<10}{'Grade':<8}{'Points':<10}",
        "-" * 60
    ]

    for c in courses:
        lines.append(
            f"{c['code']:<15}{c['unit']:<8}{c['score']:<10.1f}{c['grade']:<8}{c['weighted_point']:<10}"
        )

    lines.extend([
        "-" * 60,
        f"Total Credit Units (Semester) : {sem_units}",
        f"Total Grade Points (Semester) : {sem_points}",
        f"Semester GPA                  : {gpa:.2f}",
        f"Cumulative GPA (CGPA)         : {cgpa:.2f}",
        f"Class of Degree               : {degree_class}",
        "=" * 60
    ])

    return "\n".join(lines)


def save_to_file(report_text, student_name):
    """Saves the generated report to a text file."""
    safe_name = "_".join(student_name.strip().split()) or "student"
    filename = f"{safe_name}_CGPA_Result.txt"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(report_text)
        print(f"\nSuccess! Result saved to '{filename}'.")
    except OSError as error:
        print(f"\nWarning: Could not save file ({error}).")


def main():
    print("=== UNIVERSITY CGPA CALCULATOR ===\n")

    while True:
        name = input("Enter your full name: ").strip()
        if name:
            break
        print("Error: Name cannot be empty.")

    while True:
        department = input("Enter your department: ").strip()
        if department:
            break
        print("Error: Department cannot be empty.")

    num_courses = get_valid_int("How many courses are you offering this semester? ", min_val=1, max_val=30)

    courses, sem_units, sem_points = collect_courses(num_courses)
    gpa = round(sem_points / sem_units, 2)
    cgpa, _, _ = calculate_cgpa(sem_units, sem_points)
    degree_class = get_degree_class(cgpa)

    report = format_report(name, department, courses, sem_units, sem_points, gpa, cgpa, degree_class)
    print("\n" + report)
    save_to_file(report, name)


if __name__ == "__main__":
    main()