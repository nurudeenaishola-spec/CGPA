# University GPA & CGPA Calculator

A command-line Python application built by Ishola Nurudeen Adeola to calculate a student's semester Grade Point Average (GPA), Cumulative Grade Point Average (CGPA), and corresponding Nigerian university Class of Degree on a standard 5.0 grading scale.

## Features

- Student & Course Tracking: Collects student details (Full Name, Department) alongside course codes, credit units, and scores.
- Automated Grading & Classification: Converts numeric scores (0–100) into letter grades (A–F) and grade points (5–0), then determines the final degree classification (First Class through Pass/Fail).
- Cumulative GPA (CGPA) Support: Allows students to combine current semester results with previous semester credit units and CGPA for an accurate cumulative standing.
- Crash-Proof Input Validation: Handles invalid inputs (such as non-numeric entries, blank fields, negative numbers, or scores exceeding 100) gracefully without crashing.
- Automated Result Export: Generates a formatted academic result slip in the terminal and saves a permanent copy to <Student_Name>_CGPA_Result.txt.

## Grading & Degree Classification Scale

| Score Range | Letter Grade | Grade Point |
| :--- | :---: | :---: |
| 70 – 100 | A | 5 |
| 60 – 69 | B | 4 |
| 50 – 59 | C | 3 |
| 45 – 49 | D | 2 |
| 40 – 44 | E | 1 |
| 0 – 39 | F | 0 |

| CGPA Range (5.0 Scale) | Class of Degree |
| :--- | :--- |
| 4.50 – 5.00 | First Class Honours |
| 3.50 – 4.49 | Second Class Honours (Upper Division) |
| 2.40 – 3.49 | Second Class Honours (Lower Division) |
| 1.50 – 2.39 | Third Class Honours |
| 1.00 – 1.49 | Pass |
| Below 1.00 | Fail / Academic Probation |

## Project Structure

`text
CGPA/
├── CGPA.py          # Main application script
└── README.md        # Project documentation
