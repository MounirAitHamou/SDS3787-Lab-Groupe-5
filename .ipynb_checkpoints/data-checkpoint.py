import pandas as pd
import calendar

def is_leap_year(year):
    return calendar.isleap(year)


def is_valid_day(day, month, year):
    
    days_in_month = {
        1: 31,  
        2: 29 if is_leap_year(year) else 28,  
        3: 31,  
        4: 30,  
        5: 31,  
        6: 30, 
        7: 31, 
        8: 31,  
        9: 30,  
        10: 31, 
        11: 30,
        12: 31  
    }
    
   
    return 1 <= day <= days_in_month.get(month, 0)


data = pd.read_excel('C:/GitHub/Projects/SDS3787-Lab-Groupe-8/PIMENTO_CASES.xlsx')

invalid_dates = data[~data.apply(lambda row: is_valid_day(row['Day'], row['Month'], row['Year']), axis=1)]

if not invalid_dates.empty:
    print(f"Found {len(invalid_dates)} row(s) with invalid 'Day' value based on the month and year:")
    print(invalid_dates)
else:
    print("All rows have valid 'Day' values.")
