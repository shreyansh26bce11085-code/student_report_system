"""Individual student metrics calculation and evaluation logic."""

from config import (
    ACADEMIC_SUPPORT_LIMIT,
    ATTENDANCE_WARN_LIMIT,
    GRADE_A_MIN,
    GRADE_B_MIN,
    GRADE_C_MIN,
    HIGH_RISK_ATTENDANCE,
    HIGH_RISK_AVG,
    MED_RISK_ATTENDANCE,
    MED_RISK_AVG,
    REVISION_LIMIT,
    STUDY_HOURS_LIMIT,
)


def calculate_total(marks: tuple) -> float:
    """Calculates the sum of marks."""
    return sum(marks)


def calculate_average(marks: tuple) -> float:
    """Calculates average mark score."""
    if not marks:
        return 0.0
    return calculate_total(marks) / len(marks)


def calculate_grade(average: float) -> str:
    """Determines letter grade based on score average."""
    if average >= GRADE_A_MIN:
        return "A"
    elif average >= GRADE_B_MIN:
        return "B"
    elif average >= GRADE_C_MIN:
        return "C"
    else:
        return "D"


def calculate_risk(attendance: float, average: float) -> str:
    """Assesses academic risk level based on attendance and average."""
    if attendance < HIGH_RISK_ATTENDANCE or average < HIGH_RISK_AVG:
        return "High"
    elif attendance < MED_RISK_ATTENDANCE or average < MED_RISK_AVG:
        return "Medium"
    else:
        return "Low"


def create_recommendation(student: dict, average: float) -> list:
    """Generates tailored recommendations based on performance parameters."""
    recommendations = []

    if student["attendance"] < ATTENDANCE_WARN_LIMIT:
        recommendations.append("Improve attendance")

    if average < ACADEMIC_SUPPORT_LIMIT:
        recommendations.append("Attend extra academic support")

    if average < REVISION_LIMIT:
        recommendations.append("Revise WEAK subjects")

    if student["study_hours"] < STUDY_HOURS_LIMIT:
        recommendations.append("Increase daily study hours")

    if not recommendations:
        recommendations.append("WELL DONE! Continue the current study plan.")

    return recommendations
