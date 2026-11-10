# Read a CSV file of window cleaning employees and compute salary statistics.
# Print info about file existence and permissions before reading the file.

import csv
import os

# Check if the CSV file exists and is readable
if not os.path.exists('window_cleaning_employees.csv'):
    print(f"Error: The file 'window_cleaning_employees.csv' does not exist.")
    exit(1)  # Exit the program with an error code

if not os.access('window_cleaning_employees.csv', os.R_OK):
    print(f"Error: The file 'window_cleaning_employees.csv' is not readable.")
    exit(1)  # Exit the program with an error code

else:
    file_size = os.path.getsize('window_cleaning_employees.csv')
    print(f"The file 'window_cleaning_employees.csv' exists and is readable.")
    print(f"File size: {file_size} bytes")

csv_filename = 'window_cleaning_employees.csv'
salaries = []

# Read the CSV file and store the salaries in a list
with open(csv_filename, mode='r') as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)  # Skip the header row
    print(f"Headers: {headers}")  # Print the headers
    salary_index = headers.index("Annual_Salary")  # Find the index of the 'Annual Salary' column
    for row in reader:
        salary = float(row[salary_index])  # Convert the salary to float
        salaries.append(salary)  # Append the salary to the list

    # Compute salary stats
    avg_salary = sum(salaries) / len(salaries)  # Calculate average salary
    min_salary = min(salaries)  # Find minimum salary
    max_salary = max(salaries)  # Find maximum salary

    # Print the salary stats
    print(f"Average Salary: ${avg_salary:.2f}")
    print(f"Minimum Salary: ${min_salary:.2f}")
    print(f"Maximum Salary: ${max_salary:.2f}")