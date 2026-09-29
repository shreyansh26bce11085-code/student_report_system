"""Main entry point for running the Student Performance CLI application."""

from analytics.cohort import class_summary, count_risk_levels, find_top_students
from reports.generator import generate_student_report
from utils.input_helpers import read_float, read_int


def collect_student_data() -> list:
    """Interactively prompts and constructs a list of student records."""
    students = []
    n = read_int("Enter total number of students: ")
    while n < 1:
        print("Enter at least 1 student.")
        n = read_int("Enter total number of students: ")

    for i in range(1, n + 1):
        print(f"\n--- Input Data for Student #{i} ---")
        student = {
            "id": read_int("Enter Student ID: "),
            "name": input("Enter Student Name: "),
            "attendance": read_float("Enter Student Attendance Percentage: "),
        }

        m1 = read_float("Enter marks for Subject 1: ")
        m2 = read_float("Enter marks for Subject 2: ")
        m3 = read_float("Enter marks for Subject 3: ")
        student["marks"] = (m1, m2, m3)

        student["study_hours"] = read_float("Enter Study Hours per day: ")
        students.append(student)

    print("\nAll student data collected successfully.")
    return students


def main():
    print("=" * 46)
    print(" STUDENT PERFORMANCE & RISK ANALYSIS SYSTEM ")
    print("=" * 46)

    students = collect_student_data()

    # Cohort Analysis
    class_summary(students)

    top_student, top_avg = find_top_students(students)
    if top_student:
        print(f"Top Student   : {top_student['name']} (Avg: {round(top_avg, 2)})")

    print("Risk Breakdown:", count_risk_levels(students))

    # Output Individual Reports
    print("\nGenerating Detailed Reports...")
    for student in students:
        generate_student_report(student)


if __name__ == "__main__":
    main()
