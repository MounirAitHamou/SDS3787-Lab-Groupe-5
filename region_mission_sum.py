import pandas as pd

# Load the dataset
df = pd.read_excel('summed_PIMENTO_data_no_days.xlsx')

# Define columns to exclude for region sums
exclude_columns_region = ['MissionTitleE', 'EmployeeID', 'Month', 'Year', 'Number of entries']

# Group by GeoRegionNameE and sum the relevant columns excluding specified columns
region_sums = df.drop(columns=exclude_columns_region).groupby('GeoRegionNameE').sum(numeric_only=True)

# Save the region sums to an Excel file
region_sums.to_excel('region_sums.xlsx', sheet_name='Region Sums')

# Display the result for regions (optional)
print("Region Sums:")
print(region_sums)

# Define columns to exclude for mission sums
exclude_columns_mission = ['GeoRegionNameE', 'EmployeeID', 'Month', 'Year', 'Number of entries']

# Group by MissionTitleE and sum the relevant columns excluding specified columns
mission_sums = df.drop(columns=exclude_columns_mission).groupby('MissionTitleE').sum(numeric_only=True)

# Save the mission sums to an Excel file
mission_sums.to_excel('mission_sums.xlsx', sheet_name='Mission Sums')

# Display the result for missions (optional)
print("\nMission Sums:")
print(mission_sums)
