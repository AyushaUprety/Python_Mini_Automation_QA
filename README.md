Python Mini Automation QA Project

This project automates basic data QA checks using Python on the same CSV dataset.  
The goal is to identify missing values, duplicate emails, out-of-range ages, and negative salaries.

Dataset:
- Columns: Name, Gender, Age, City, Department, Salary, Email
- 500 data rows

Checks Performed:
- Counted total rows
- Checked for missing values in all columns
- Detected duplicate emails
- Flagged ages outside 18-100
- Flagged negative salaries

Sample Output:
Total rows: 500
Missing values per column: {'Name': 0, 'Gender': 0, 'Age': 248, 'City': 0, 'Department': 0, 'Salary': 252, 'Email': 0}
Duplicate emails found in rows: [54, 64, 97, ...]
Out-of-range ages in rows: [2, 3, 4, ...]
Negative salaries in rows: []


