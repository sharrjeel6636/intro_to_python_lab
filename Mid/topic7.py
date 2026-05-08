# topic7.py – Student Report Card Generator

"""Interactive script that collects a student's marks for a set of subjects
and prints a formatted report card.

Features implemented per assignment requirements:
- Average calculated and displayed with two-decimal precision
- Final grade obtained via the get_grade helper
- Highest and lowest subject/mark identified without using max/min
- Personalized message based on the grade
- Visual separators made of = and - characters
- Clean, well-commented sections for readability
"""

# ------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------

def get_grade(average: float) -> str:
    """Return a letter grade for average using the standard scale.

    - A : average >= 80
    - B : 65 <= average < 80
    - C : 50 <= average < 65
    - D : 40 <= average < 50
    - F : average < 40
    """
    if average >= 80:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

def personalized_message(grade: str) -> str:
    """Return a brief message tailored to the supplied grade."""
    messages = {
        "A": "Excellent work! Keep it up.",
        "B": "Well done! A little more effort for an A.",
        "C": "Good effort, but there is room for improvement.",
        "D": "You passed, consider reviewing the material.",
        "F": "You need to improve. Seek help and keep practicing.",
    }
    return messages.get(grade, "")

# ------------------------------------------------------------
# Main execution block
# ------------------------------------------------------------

def main() -> None:
    print("=" * 40)
    print(f"{'Student Report Card Generator':^40}")
    print("=" * 40)

    # --------------------------------------------------------
    # Input collection
    # --------------------------------------------------------
    name = input("Enter Student Name: ").strip().title()

    # Collect marks for each subject with validation
    math_mark = None
    python_mark = None
    physics_mark = None
    english_mark = None

    for subject, var_name in [("Math", "math_mark"), ("Python", "python_mark"),
                               ("Physics", "physics_mark"), ("English", "english_mark")]:
        while True:
            try:
                raw = input(f"Enter marks for {subject} (0-100): ")
                mark = int(raw)
                if 0 <= mark <= 100:
                    if var_name == "math_mark":
                        math_mark = mark
                    elif var_name == "python_mark":
                        python_mark = mark
                    elif var_name == "physics_mark":
                        physics_mark = mark
                    elif var_name == "english_mark":
                        english_mark = mark
                    break
                else:
                    print("Error: Marks must be between 0 and 100.")
            except ValueError:
                print("Error: Please enter a valid numerical value.")

    # Store all data in a single dictionary as per requirements
    student = {
        'name': name,
        'Math': math_mark,
        'Python': python_mark,
        'Physics': physics_mark,
        'English': english_mark
    }

    # --------------------------------------------------------
    # Calculations
    # --------------------------------------------------------
    # Extract only the subject marks (exclude 'name' key)
    subject_marks = {k: v for k, v in student.items() if k != 'name'}

    total = sum(subject_marks.values())
    average = round(total / len(subject_marks), 2)  # two-decimal average
    grade = get_grade(average)

    # Determine highest and lowest subject using a manual loop (no max/min allowed)
    first_subj, first_mark = next(iter(subject_marks.items()))
    highest_mark = first_mark
    highest_subj = first_subj
    lowest_mark = first_mark
    lowest_subj = first_subj

    for sub, mark in list(subject_marks.items())[1:]:
        if mark > highest_mark:
            highest_mark = mark
            highest_subj = sub
        if mark < lowest_mark:
            lowest_mark = mark
            lowest_subj = sub

    # --------------------------------------------------------
    # Output report
    # --------------------------------------------------------
    print("\n" + "=" * 40)
    print(f"{'STUDENT REPORT CARD':^40}")
    print("=" * 40)
    print(f"Name: {student['name']}")
    print("-" * 40)
    for sub, mark in subject_marks.items():
        print(f"{sub:<15}: {mark:>7.2f}")
    print("-" * 40)
    print(f"Total Marks    : {total:>7.2f}")
    print(f"Average        : {average:>7.2f}")
    print(f"Highest Mark   : {highest_subj} ({highest_mark:>5.2f})")
    print(f"Lowest Mark    : {lowest_subj} ({lowest_mark:>5.2f})")
    print(f"Final Grade    : {grade:>5}")
    print(f"Message        : {personalized_message(grade)}")
    print("=" * 40)
    print(f"{'PROMOTED' if grade != 'F' else 'RETAINED':^40}")
    print("=" * 40)

if __name__ == "__main__":
    main()