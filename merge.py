import pandas as pd

# Load your datasets from Excel files
cases_df = pd.read_excel('PIMENTO_CASES.xlsx')
programs_df = pd.read_excel('PIMENTO_PROGRAMS.xlsx')

# Merge the datasets on the specified attributes using an outer join
merged_df = pd.merge(
    cases_df, 
    programs_df, 
    how='outer', 
    on=['GeoRegionNameE', 'MissionTitleE', 'EmployeeID', 'Month', 'Day', 'Year']
)

# Handle the 'Other' variable by summing the values from both datasets
# If either 'Other' column is NaN, it will be treated as 0 for the summation
merged_df['Other'] = merged_df['Other_x'].fillna(0) + merged_df['Other_y'].fillna(0)

# Drop the old 'Other_x' and 'Other_y' columns
merged_df = merged_df.drop(columns=['Other_x', 'Other_y'])

# Display the merged dataframe
print(merged_df)

# Save the result to a new file
merged_df.to_excel('merged_PIMENTO_data.xlsx', index=False)
