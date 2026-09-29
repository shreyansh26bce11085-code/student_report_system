# Student Performance & Risk Analysis System

## Overview

The **Student Performance & Risk Analysis System** is a CLI-based Python application designed to collect, process, and analyze student academic data. It computes individual subject averages, assigns letter grades, evaluates academic risk levels based on attendance and performance, and outputs personalized improvement recommendations. Additionally, it provides class-wide statistics, including class averages, top-performer identification, and risk distribution summaries.

---

## Features

* **Robust Input Validation:** Ensures error-free numeric inputs for Student ID, attendance percentage, marks, and daily study hours using recursive prompt handling.
* **Academic Evaluation:** Automatically calculates total marks, average scores, and assigns corresponding letter grades (`A`, `B`, `C`, `D`).
* **Risk Level Assessment:** Categorizes students into **High**, **Medium**, or **Low** risk levels based on attendance thresholds and grade averages.
* **Personalized Recommendations:** Generates customized action items (e.g., attendance warnings, revision alerts, study hour adjustments) tailored to individual student metrics.
* **Class-Wide Analytics:** Computes total class average, identifies the top-performing student, and tallies overall risk counts.
* **Comprehensive Reporting:** Outputs structured, easy-to-read individual performance reports for all enrolled students.

---

## Technologies & Tools Used

* **Programming Language:** Python 3.x
* **Dependencies:** None (Uses standard Python library components: `tuples`, `dictionaries`, `lists`, control flow structures, and standard `sys` input/output handling).

---

## Installation & Setup

### Prerequisites

Ensure you have Python 3 installed on your machine. You can verify your installation by running:

```bash
python --version
# or
python3 --version

```

### Steps to Run

1. **Clone or Download the Repository:**
```bash
git clone https://github.com/your-username/student-performance-analyzer.git
cd student-performance-analyzer

```


2. **Run the Script:**
Execute the Python file using your CLI:
```bash
python main.py

```



---

## Testing Instructions

To verify the system functionality, follow these manual test scenarios during prompt execution:

| Test Case | Inputs / Scenario | Expected Outcome |
| --- | --- | --- |
| **Invalid Input Handling** | Enter letters (e.g., `"abc"`) when prompted for Attendance or ID. | Script catches `ValueError` and reprompts: *"Please enter a number."* |
| **High Risk Student** | Attendance: `55%`, Marks: `40, 45, 50` (Avg: `45`) | Grade: `D`, Risk Level: `High`, Recommendations: Attendance warning, academic support, and extra study hours. |
| **Low Risk / Top Student** | Attendance: `90%`, Marks: `90, 85, 95` (Avg: `90`) | Grade: `A`, Risk Level: `Low`, Recommendation: *"WELL DONE! Continue current study plan."* |
| **Class Summary Batch** | Input `N = 2` students with varying marks. | Generates accurate combined class average, identifies the top student, and prints the overall risk dictionary count. |

---
