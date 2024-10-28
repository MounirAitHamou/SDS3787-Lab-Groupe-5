import pandas as pd

# Load the dataset
file_path = "filled_PIMENTO_data.xlsx"
df = pd.read_excel(file_path)

# Specify the columns to check for non-numeric values
columns_to_check = [
    'Disasters', 'Disasters Time', 'Death', 'Death Time',
    'Assistance Communications', 'Assistance Communications Time',
    'Legal/Notary', 'Legal/NotaryTime', 'Evacuation', 'Evacuation  Time',
    'Child Abduction/Custody', 'Child Abduction/Custody Time',
    'Family Distress', 'Family Distress Time', 'Registration', 'Registration Time',
    'Immigration_x', 'Immigration Time', 'Arrest', 'Arrest Time',
    'Citizenship', 'Citizenship Time', 'Passport', 'Passport Time',
    'Service', 'Service Time', 'Financial Assistance/Transfers', 
    'Financial Assistance/Transfers Time', 'Emergency', 'Program_Mgmt',
    'Liaison', 'Visit_Mgmt', 'Pol_Econ', 'Comm_Trade', 'Development',
    'Police', 'Immigration_y', 'Informatics', 'Program_Services',
    'Public_Comms', 'Training', 'Other'
]

# Function to find rows with non-numeric values in specified columns
def find_non_numeric_rows(df, columns):
    non_numeric_rows = df[~df[columns].apply(pd.to_numeric, errors='coerce').notnull().all(axis=1)]
    return non_numeric_rows

# Get rows with non-numeric values
non_numeric_rows = find_non_numeric_rows(df, columns_to_check)

# Print the rows with non-numeric values
if not non_numeric_rows.empty:
    print("Rows with non-numeric values:")
    print(non_numeric_rows)
else:
    print("No rows with non-numeric values found in the specified columns.")
