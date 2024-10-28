import pandas as pd

# Reading the Excel file
df = pd.read_excel('PIMENTO_PROGRAMS.xlsx', engine='openpyxl')

# Filtering the relevant columns and dropping missing values
df_filtered = df[['Year','Emergency', 'Program_Mgmt', 'Visit_Mgmt', 'Training']]
df_filtered = df_filtered.dropna()

# Grouping and summing up the filtered data
data_to_store = df_filtered.groupby('Year')[['Emergency', 'Program_Mgmt', 'Visit_Mgmt', 'Training']].sum().reset_index()

# Saving the first dataset to an Excel file
data_to_store.columns = ['Year','Emergency', 'Program_Mgmt', 'Visit_Mgmt', 'Training']
data_to_store.to_excel('firstdataset.xlsx', index=False)

# Filtering another set of columns and dropping missing values
df_filtered2 = df[['MissionTitleE', 'Comm_Trade', 'Development', 'Police','Informatics']]
df_filtered2 = df_filtered2.dropna()

# Grouping and summing up the second filtered data
data_to_store2 = df_filtered2.groupby('MissionTitleE')[['Comm_Trade', 'Development', 'Police','Informatics']].sum().reset_index()

# Saving the second dataset to an Excel file
data_to_store2.columns = ['MissionTitleE', 'Comm_Trade', 'Development', 'Police','Informatics']
data_to_store2.to_excel('seconddataset.xlsx', index=False)
