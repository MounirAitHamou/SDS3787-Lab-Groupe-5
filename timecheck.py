import pandas as pd

# Load the dataset
file_path = "updated_PIMENTO_data.xlsx"
df = pd.read_excel(file_path)

# Function to calculate the total time worked in minutes based on time columns
def calculate_total_minutes(row):
    time_columns = [col for col in df.columns if 'Time' in col]  # Assuming these columns represent time in minutes
    total_minutes = row[time_columns].sum()
    return total_minutes

# Function to check consecutive workdays for employees (time in minutes)
def check_consecutive_minutes(df, max_minutes):
    consecutive_violations = []
    
    # Sort data by EmployeeID and Date (assuming Month/Day/Year fields exist to construct date)
    
    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']], format='%Y%m%d', errors='coerce')
    


    df_sorted = df.sort_values(by=['EmployeeID', 'Date'])
    
    # Calculate total minutes for each row and add it to a new column
    df_sorted['TotalMinutes'] = df_sorted.apply(calculate_total_minutes, axis=1)
    
    # Group by EmployeeID and iterate over each employee's rows (their shifts)
    for employee_id, group in df_sorted.groupby('EmployeeID'):
        group = group.reset_index()  # Reset index for easier row-wise access
        
        for i in range(1, len(group)):
            total_minutes_current_day = group.loc[i, 'TotalMinutes']
            total_minutes_previous_day = group.loc[i - 1, 'TotalMinutes']
            
            # Assuming consecutive workday if difference between dates is 1 day
            if (group.loc[i, 'Date'] - group.loc[i - 1, 'Date']).days == 1:
                # Check if total minutes exceed max allowed minutes in a row
                if total_minutes_current_day + total_minutes_previous_day > max_minutes:
                    consecutive_violations.append(group.loc[i].name)  # Append index of the violation
    
    return consecutive_violations

# Set the maximum number of minutes allowed in a row
MAX_MINUTES =  * 60  # Adjust this based on your threshold (12 hours = 720 minutes)

with open("output_timecheck.txt", "w") as f:
   
    consecutive_violations = check_consecutive_minutes(df, MAX_MINUTES)
    if consecutive_violations:
        f.write(f"Employees working more than {MAX_MINUTES / 60} hours in a row found at indices:\n")
        f.write(', '.join(map(str, consecutive_violations)) + '\n')

    # Summary
    print("Error detection complete. Please check the printed row indices for manual correction.")
