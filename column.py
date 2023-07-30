import pandas as pd
import sys

# Get the column name as a parameter
file_name = sys.argv[1]
column_name = sys.argv[2]

# Read the CSV file
df = pd.read_csv(file_name)

# Get unique values in the column
unique_values = df[column_name].unique()

# Print unique values
for value in unique_values:
        print(value)
