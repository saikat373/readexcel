import pandas as pd

# Load the Excel file
file_path = "./excel/Employee.xlsx"  # Change to your actual file path
df = pd.read_excel(file_path)

# Find missing values
missing_data = df.isnull()

# Iterate through each column and find missing values with row numbers
for column in df.columns:
    missing_rows = df.index[missing_data[column]].tolist()  # Get row indices where data is missing
    if missing_rows:
        print(f"Column '{column}' has missing values at row(s): {', '.join(map(str, [r+2 for r in missing_rows]))}")  
        # Adding 2 because Excel index starts from 1 and there's a header row

if missing_data.any().sum() == 0:
    print("No missing values found!")
