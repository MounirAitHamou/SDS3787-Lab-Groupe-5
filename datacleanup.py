import pandas as pd

# Load the dataset
file_path = "PIMENTO_CASES.xlsx"
df = pd.read_excel(file_path)

# Function to calculate the total hours worked in a row based on time columns (assuming these represent hours)
def calculate_total_hours(row):
    time_columns = [col for col in df.columns if 'Time' in col]  # Assuming these are hours worked per task
    total_hours = row[time_columns].sum()
    return total_hours

# Function to check consecutive workdays for employees
def check_consecutive_hours(df, max_hours):
    consecutive_violations = []
    
    # Sort data by EmployeeID and Date (assuming Month/Day/Year fields exist to construct date)
    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
    df_sorted = df.sort_values(by=['EmployeeID', 'Date'])
    
    # Group by EmployeeID and iterate over each employee's rows (their shifts)
    for employee_id, group in df_sorted.groupby('EmployeeID'):
        group = group.reset_index()  # Reset index for easier row-wise access
        
        for i in range(1, len(group)):
            total_hours_current_day = calculate_total_hours(group.loc[i])
            total_hours_previous_day = calculate_total_hours(group.loc[i - 1])
            
            # Assuming consecutive workday if difference between dates is 1 day
            if (group.loc[i, 'Date'] - group.loc[i - 1, 'Date']).days == 1:
                # Check if total hours exceed max allowed hours in a row
                if total_hours_current_day + total_hours_previous_day > max_hours:
                    consecutive_violations.append(group.loc[i].name)  # Append index of the violation
    
    return consecutive_violations

# Set the maximum number of hours allowed in a row
MAX_HOURS = 12  # Adjust this based on your threshold

# Prepare to write errors to output.txt
with open("output.txt", "w") as f:

    # 1. Duplicate Check
    duplicates = df[df.duplicated()]
    if not duplicates.empty:
        f.write("Duplicate rows found at indices:\n")
        f.write(', '.join(map(str, duplicates.index.tolist())) + '\n')

    # 2. Missing Values Check
    missing_values = df[df.isnull().any(axis=1)]
    if not missing_values.empty:
        f.write("Rows with missing values found at indices:\n")
        f.write(', '.join(map(str, missing_values.index.tolist())) + '\n')

    # 3. Invalid Month Check
    invalid_months = df[(df['Month'] < 1) | (df['Month'] > 12)]
    if not invalid_months.empty:
        f.write("Invalid Month values found at row indices:\n")
        f.write(', '.join(map(str, invalid_months.index.tolist())) + '\n')

    # 4. Invalid Day Check
    invalid_days = df[(df['Day'] < 1) | (df['Day'] > 31)]
    if not invalid_days.empty:
        f.write("Invalid Day values found at row indices:\n")
        f.write(', '.join(map(str, invalid_days.index.tolist())) + '\n')

    # 5. Non-Numeric EmployeeID Check
    non_numeric_employee_ids = df[pd.to_numeric(df['EmployeeID'], errors='coerce').isnull()]
    if not non_numeric_employee_ids.empty:
        f.write("Non-numeric EmployeeID found at row indices:\n")
        f.write(', '.join(map(str, non_numeric_employee_ids.index.tolist())) + '\n')

    # 6. Negative Time Values Check
    time_columns = [col for col in df.columns if 'Time' in col]
    for col in time_columns:
        invalid_times = df[df[col] < 0]
        if not invalid_times.empty:
            f.write(f"Invalid values in column '{col}' found at row indices:\n")
            f.write(', '.join(map(str, invalid_times.index.tolist())) + '\n')

    # 7. Check for employees working too many consecutive hours
    consecutive_violations = check_consecutive_hours(df, MAX_HOURS)
    if consecutive_violations:
        f.write(f"Employees working more than {MAX_HOURS} hours in a row found at indices:\n")
        f.write(', '.join(map(str, consecutive_violations)) + '\n')

    # Summary
    f.write("Error detection complete. Please check the printed row indices for manual correction.\n")
