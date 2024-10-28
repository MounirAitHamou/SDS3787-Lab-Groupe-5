import pandas as pd

# Load the dataset
file_path = 'updated_PIMENTO_data.xlsx'  # Adjust this path as necessary
df = pd.read_excel(file_path)

# Group by GeoRegionNameE, MissionTitleE, EmployeeID, Month, Year
grouped_df = df.groupby(['GeoRegionNameE', 'MissionTitleE', 'EmployeeID', 'Month', 'Year'], as_index=False).sum()

# Optional: Save the aggregated data to a new Excel file
output_file_path = 'summed_PIMENTO_data_no_days.xlsx'
grouped_df.to_excel(output_file_path, index=False)

# Display the first few rows of the resulting DataFrame
print(grouped_df.head())