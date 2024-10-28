import pandas as pd

# Load Excel files efficiently into pandas DataFrames
df1 = pd.read_excel('PIMENTO_CASES.xlsx', engine='openpyxl')  # Specify engine for efficiency
df2 = pd.read_excel('PIMENTO_PROGRAMS.xlsx', engine='openpyxl')

# Perform an inner join to keep only matching rows
merged_df = pd.merge(df1, df2, on=['GeoRegionNameE', 'MissionTitleE', 'EmployeeCode', 'Month', 'Day', 'Year'], how='inner')

# Save the result to a new Excel file using compression for smaller size
merged_df.to_excel('merged_dataset.xlsx', index=False, engine='openpyxl')

print("Datasets successfully merged!")
