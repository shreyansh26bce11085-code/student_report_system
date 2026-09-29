"""Report output formatting module."""

from analytics.evaluators import (
    calculate_average,
    calculate_grade,
    calculate_risk,
    create_recommendation,
)


def generate_student_report(student: dict) -> None:
    """Displays a formatted academic performance report for an individual student."""
    avg = calculate_average(student["marks"])
    grade = calculate_grade(avg)
    risk = calculate_risk(student["attendance"], avg)

    print("\n" + "=" * 40)
    print("         STUDENT PERFORMANCE REPORT")
    print("=" * 40)
    print(f"Student Name : {student['name']}")
    print(f"Student ID   : {student['id']}")
    print(f"Attendance   : {student['attendance']}%")
    print(f"Marks        : {student['marks']}")
    print(f"Study Hours  : {student['study_hours']} hrs/day")
    print(f"Average Mark : {round(avg, 2)}")
    print(f"Grade        : {grade}")
    print(f"Risk Level   : {risk}")
    print("-" * 40)
    print("Recommendations:")
    for item in create_recommendation(student, avg):
        print(f"  - {item}")
    print("=" * 40)
