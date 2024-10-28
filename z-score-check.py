import pandas as pd
import numpy as np
import os

def main():
    rowsyouwanttosee = int(input("Enter the number of rows you want to see per variable: "))
    if rowsyouwanttosee <= 0:
        print("Please enter a positive number")
        return

    filename = input("Enter the name of the file: ")
    if not filename.endswith('.xlsx'):
        filename += '.xlsx'

    if not os.path.exists(filename):
        print(f"File {filename} not found")
        return

    print(f"Reading file: {filename}, looking for {rowsyouwanttosee} outliers per variable")

    df = pd.read_excel(filename)
    numeric_cols = df.select_dtypes(include=[np.number])

    z_scores = (numeric_cols - numeric_cols.mean()) / numeric_cols.std()

    outliers_df = pd.DataFrame()

    for col in numeric_cols.columns:
   
        sorted_z_scores = z_scores[col].abs().sort_values(ascending=False)
        
        top_outliers_indices = sorted_z_scores.head(rowsyouwanttosee).index
        df_outliers = df.loc[top_outliers_indices].copy()
        df_outliers['Outlier_Column'] = col  
        
        # Reorder the columns so that 'Outlier_Column' is the first column
        cols = ['Outlier_Column'] + [c for c in df_outliers.columns if c != 'Outlier_Column']
        df_outliers = df_outliers[cols]
        
        outliers_df = pd.concat([outliers_df, df_outliers], ignore_index=True)

    if not outliers_df.empty:
        output_filename = "outliers_report_" + filename
        outliers_df.to_excel(output_filename, index=False)
        print(f"Outliers have been saved into '{output_filename}'")
    else:
        print("No outliers found in any columns.")

if __name__ == "__main__":
    main()
