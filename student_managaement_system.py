def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


student = {}

student["id"] = read_int("Enter Student ID:")
student["name"] = input("Enter Student Name:")
student["attendance"] = read_float("Enter Student Attendance Percentage:")
m1 = read_float("Enter marks of student in subject 1:")
m2 = read_float("Enter marks of student in subject 2:")
m3 = read_float("Enter marks of student in subject 3:")
student["marks"] = (m1, m2, m3)
student["study_hours"] = read_float("Enter Student Study Hours per day:")

print("Student Data Saved Successfully.")
print(student)



def calculate_total(marks):
    total = 0

    for mark in marks:
        total = total + mark

    return total

def calculate_average(marks):
    total = calculate_total(marks)
    return total / len(marks)

print("Student:", student ["name"])
print("Marks:", student["marks"])
print("Total:", calculate_total(student["marks"]))
print("Average:", round(calculate_average(student["marks"]),2))


def calculate_grade(average):
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >=50:
        return "C"
    else:
        return "D"


average = calculate_average(student["marks"])
grade = calculate_grade(average)

print("Average:", round(average, 2))
print("Grade:", grade)


def calculate_risk(attendance, average):
    if attendance < 60 or average < 50:
        return "High"
    elif attendance < 75 or average < 60:
        return "Medium"
    else:
        return "Low"


risk = calculate_risk(student["attendance"], average)
print("Risk Level:", risk)


def create_recommendation(student, average):
    recommendations = []

    if student["attendance"] < 75:
        recommendations.append("Improve attendance")

    if average < 50:
        recommendations.append("Attend extra academic support")


    if average < 65:
        recommendations.append("Revise WEAK subjects")

    if student["study_hours"]<3:
        recommendations.append("Increase daily study hours")

    if len(recommendations) == 0:
        recommendations.append("WELL DONE! Continue the current study plan.")

    return recommendations

recommendations = create_recommendation(student,  average)

print("Recommendations (according to me):")
for item in recommendations:
    print("-", item)


students = []

n = read_int("Enter total number of students:")
while n < 1:
    print("Enter at least 1 student.")
    n = read_int("Enter total number of students:")

for i in range(n):
    student = {}
    student["id"] = read_int("Enter Student ID:")
    student["name"] = input("Enter Student Name:")
    student["attendance"] = read_float("Enter the Student attendance percentage:")
    m1 = read_float("Enter the marks obtained by Student in Subject 1: ")
    m2 = read_float("Enter the marks obtained by Student in Subject 2: ")
    m3 = read_float("Enter the marks obtained by Student in Subject 3: ")
    student["marks"] = (m1, m2, m3)
    student["study_hours"] = read_float("Enter study hours per day: ")
    students.append(student)

print("All students data is stored.")
print(students)


def class_summary(students):
    total_average = 0

    for student in students:
        avg = calculate_average(student["marks"])
        total_average = total_average + avg


    class_average = total_average / len(students)
    print("Class Average:", round(class_average, 2))
    print("Total Students:", len(students))
    print("Number of students in input:", len(students))


class_summary(students)


def find_top_students(students):
    top_student = students[0]
    top_average = calculate_average(top_student["marks"])

    for student in students[1:]:
        current_average = calculate_average(student["marks"])

        if current_average > top_average:
            top_student = student
            top_average = current_average

    return top_student, top_average

best_students, best_average = find_top_students(students)
print("Top Student:", best_students["name"])
print("Top Average:" , round(best_average, 2))


def count_risk_levels(students):
    risk_counts = {
        "Low": 0,
        "Medium": 0,
        "High": 0
    }
    for student in students:
        avg = calculate_average(student["marks"])
        risk = calculate_risk(student["attendance"], avg)

        if risk == "Low":
            risk_counts["Low"] += 1
        elif risk == "Medium":
            risk_counts["Medium"] += 1
        else:
            risk_counts["High"] += 1

    return risk_counts

print("Risk Counts:", count_risk_levels(students))


def generate_student_report(student):
    avg = calculate_average(student["marks"])
    grade = calculate_grade(avg)
    risk = calculate_risk(student["attendance"], avg)

    print("Student Name:", student["name"])
    print("Student ID:", student["id"])
    print("Attendance:", student["attendance"])
    print("Marks:", student["marks"])
    print("Study Hours:", student["study_hours"])
    print("Average:", round(avg, 2))
    print("Grade:", grade)
    print("Risk Level:", risk)

    recommendations = create_recommendation(student, avg)
    print("Recommendations:")
    for item in recommendations:
        print("-", item)

    print("-" * 30)


for student in students:
    generate_student_report(student)
