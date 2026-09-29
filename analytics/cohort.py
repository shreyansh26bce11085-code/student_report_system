"""Cohort-level analytics and aggregated metrics."""

from analytics.evaluators import calculate_average, calculate_risk


def class_summary(students: list) -> None:
    """Prints total student count and overall class average score."""
    if not students:
        print("No student data available.")
        return

    total_average = sum(calculate_average(s["marks"]) for s in students)
    class_average = total_average / len(students)

    print("\n--- Class Summary ---")
    print("Class Average :", round(class_average, 2))
    print("Total Students:", len(students))


def find_top_students(students: list) -> tuple:
    """Finds the student with the highest average score."""
    if not students:
        return None, 0.0

    top_student = students[0]
    top_average = calculate_average(top_student["marks"])

    for student in students[1:]:
        current_average = calculate_average(student["marks"])
        if current_average > top_average:
            top_student = student
            top_average = current_average

    return top_student, top_average


def count_risk_levels(students: list) -> dict:
    """Aggregates students count by risk levels (Low, Medium, High)."""
    risk_counts = {"Low": 0, "Medium": 0, "High": 0}
    for student in students:
        avg = calculate_average(student["marks"])
        risk = calculate_risk(student["attendance"], avg)
        if risk in risk_counts:
            risk_counts[risk] += 1

    return risk_counts
