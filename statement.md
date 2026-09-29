# Project Statement & Scope

## Problem Statement

In educational settings, manually tracking student academic progress, attendance records, and study habits is labor-intensive and susceptible to human error. Educators and academic advisors often lack efficient tools to quickly evaluate overall student health, flag at-risk individuals early, and deliver actionable, personalized feedback. Without automated assessment mechanisms, timely academic intervention and clear performance visibility across cohorts remain significant challenges.

---

## Scope of the Project

The **Student Performance & Risk Analysis System** provides a lightweight, command-line interface (CLI) environment to automate student evaluations and classroom analytics.

* **In-Scope:**
* Interactive CLI input ingestion with robust numerical validation.
* Individual metric calculation (totals, averages, letter grades).
* Dual-variable risk classification based on attendance percentage and academic score averages.
* Rule-based generation of targeted academic improvement recommendations.
* Batch processing of student cohorts to calculate class averages, distribution of risk levels, and top-student identification.
* Terminal-formatted individual performance reports.


* **Out-of-Scope:**
* Graphical User Interface (GUI) or web portal integration.
* Persistent database storage (data exists in runtime memory during execution).
* Automated external messaging or email notification services.



---

## Target Users

* **Educators & Tutors:** To rapidly calculate grades, review performance metrics, and pinpoint students needing academic interventions.
* **Academic Advisors & Counselors:** To identify attendance trends, study habit gaps, and risk levels for targeted counseling sessions.
* **Course Coordinators:** To analyze cohort-level statistics, assess pass/risk ratios, and monitor overall teaching outcomes.

---

## High-Level Features

* **Validated Input Handling:** Enforces correct numeric datatypes for student IDs, attendance, marks, and daily study hours using error-trapping retry loops.
* **Academic Grading Engine:** Automatically calculates total scores and mean performance, mapping results to letter grades ($A \ge 85\%$, $B \ge 70\%$, $C \ge 50\%$, $D < 50\%$).
* **Risk Categorization Matrix:** Evaluates combined attendance and grade average thresholds to assign **Low**, **Medium**, or **High** risk levels to students.
* **Targeted Recommendation Engine:** Evaluates individual metrics against intervention benchmarks (e.g., study hours $< 3$, attendance $< 75\%$, average score $< 50\%$) to generate tailored advice.
* **Cohort-Wide Analytics:** Aggregates class data to output overall class averages, total student counts, top-performer rankings, and risk-level counts.
* **Automated Individual Reporting:** Prints comprehensive, standardized summary reports for every student in the system.
