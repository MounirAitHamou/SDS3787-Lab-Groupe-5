import pandas as pd
import numpy as np
import os

def main():
    filename = input("Enter the name of the file: ")
    if not filename.endswith('.xlsx'):
        filename += '.xlsx'

    if not os.path.exists(filename):
        print(f"File {filename} not found")
        return
    print(f"Reading file: {filename}")
    df = pd.read_excel(filename)
    #check that each employee does not work too many hours per day in a row
    

    return




if __name__ == "__main__":
    main()
