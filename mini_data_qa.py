import csv

file_path = "data.csv"  # make sure your CSV is here

with open(file_path, newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    rows = list(reader)

total_rows = len(rows)
missing_counts = {}
duplicate_Emails = []
seen_Emails = set()
out_of_range_Ages = []
negative_Salaries = []


for col in reader.fieldnames:
    missing_counts[col] = 0

for i, row in enumerate(rows, start=2):  
    # Missing values
    for col in reader.fieldnames:
        if row[col] == "" or row[col] is None:
            missing_counts[col] += 1

    # Duplicate emails
    Email = row["Email"]
    if Email in seen_Emails:
        duplicate_Emails.append(i)
    else:
        seen_Emails.add(Email)

    # Out-of-range ages
    if row["Age"] != "":
        try:
            Age = int(row["Age"])
            if Age < 18 or Age > 100:
                out_of_range_Ages.append(i)
        except:
            out_of_range_Ages.append(i)

    # Negative salary
    if row["Salary"] != "":
        try:
            Salary = float(row["Salary"])
            if Salary < 0:
                negative_Salaries.append(i)
        except:
            pass


print("Total rows:", total_rows)
print("Missing values per column:", missing_counts)
print("Duplicate emails found in rows:", duplicate_Emails)
print("Out-of-range ages in rows:", out_of_range_Ages)
print("Negative salaries in rows:", negative_Salaries)
