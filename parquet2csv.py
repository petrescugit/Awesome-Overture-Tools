import pandas as pd
from fastparquet import ParquetFile
import sys

def convert_parquet_to_csv(input_file, output_file):
    # Read the parquet file with fastparquet
    pf = ParquetFile(input_file)
    df = pf.to_pandas()

    # Write to a csv file
    df.to_csv(output_file, index=False)

# Entry point of the script
if __name__ == "__main__":
    # Check if the script received the correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python3 convert.py <input_file.parquet> <output_file.csv>")
        sys.exit(1)

    # Extract arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Call the conversion function
    convert_parquet_to_csv(input_file, output_file)
