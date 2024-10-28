import pandas as pd

# Load the dataset
df = pd.read_excel('summed_PIMENTO_data_no_days.xlsx')

# Define columns to exclude for region sums
exclude_columns_employee = ['MissionTitleE', 'GeoRegionNameE', 'Month', 'Year', 'Number of entries']

# Group by GeoRegionNameE and sum the relevant columns excluding specified columns
region_sums = df.drop(columns=exclude_columns_employee).groupby('EmployeeID').sum(numeric_only=True)

# Save the region sums to an Excel file
region_sums.to_excel('employee_sums.xlsx', sheet_name='Employee Sums')

# Display the result for regions (optional)
print("Region Sums:")
print(region_sums)