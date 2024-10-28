import pandas as pd

# Load the dataset
data = pd.read_excel('summed_PIMENTO_data_no_days.xlsx')

# Example: Group by Region, Mission, and Employee
grouped_region = data.groupby('GeoRegionNameE')
grouped_mission = data.groupby('MissionTitleE')
grouped_employee = data.groupby('EmployeeID')

# Aggregation calculations
aggregated_data = {
    'Total Entries': data['Number of entries'].sum(),
    'Total Disasters': data['Disasters'].sum(),
    'Total Deaths': data['Death'].sum(),
    'Total Assistance Communications': data['Assistance Communications'].count(),
    'Total Legal Notary': data['Legal/Notary'].count(),
    'Total Child Abduction Custody': data['Child Abduction/Custody'].count(),
    'Total Services Provided': data['Service'].count(),
    'Total Financial Assistance': data['Financial Assistance/Transfers'].count(),
}

# Calculate rates and averages for each grouping
def calculate_aggregates(group):
    return {
        'Disaster Rate': group['Disasters'].sum() / group['Number of entries'].sum() if group['Number of entries'].sum() > 0 else 0,
        'Avg Disaster Time': group['Disasters Time'].sum() / group['Disasters'].sum() if group['Disasters'].sum() > 0 else 0,
        'Death Rate': group['Death'].sum() / group['Number of entries'].sum() if group['Number of entries'].sum() > 0 else 0,
        'Assistance Comm Frequency': group['Assistance Communications'].count() / group['Number of entries'].sum() if group['Number of entries'].sum() > 0 else 0,
        'Legal Intervention Rate': group['Legal/Notary'].count() / group['Number of entries'].sum() if group['Number of entries'].sum() > 0 else 0,
        'Child Abduction Rate': group['Child Abduction/Custody'].count() / group['Number of entries'].sum() if group['Number of entries'].sum() > 0 else 0,
    }

# Apply the aggregate calculations
region_aggregates = grouped_region.apply(calculate_aggregates)
mission_aggregates = grouped_mission.apply(calculate_aggregates)
employee_aggregates = grouped_employee.apply(calculate_aggregates)

# Combine results into DataFrames
region_aggregates_df = pd.DataFrame(region_aggregates.tolist(), index=region_aggregates.index)
mission_aggregates_df = pd.DataFrame(mission_aggregates.tolist(), index=mission_aggregates.index)
employee_aggregates_df = pd.DataFrame(employee_aggregates.tolist(), index=employee_aggregates.index)

# Display the results
print("Region Aggregates:")
print(region_aggregates_df)
print("\nMission Aggregates:")
print(mission_aggregates_df)
print("\nEmployee Aggregates:")
print(employee_aggregates_df)

# Save the aggregated data to Excel
with pd.ExcelWriter('aggregated_data.xlsx') as writer:
    region_aggregates_df.to_excel(writer, sheet_name='Region Aggregates')
    mission_aggregates_df.to_excel(writer, sheet_name='Mission Aggregates')
    employee_aggregates_df.to_excel(writer, sheet_name='Employee Aggregates')
