import pandas as pd

# Load the Excel file
file_path = 'merged_PIMENTO_data.xlsx'

df = pd.read_excel(file_path)

# Remove duplicate rows
df_cleaned = df.drop_duplicates()

# Save the cleaned DataFrame to a new Excel file
output_file_path = 'unduped_PIMENTO_data.xlsx'
df_cleaned.to_excel(output_file_path, index=False)

print(f"Duplicate rows removed. Cleaned data saved to {output_file_path}.")
