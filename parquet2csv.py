import duckdb
import sys

def convert_parquet_to_csv(input_path, output_path):
    # Connect to DuckDB
    conn = duckdb.connect()

    # Prepare the query to read from Parquet files
    query = f"SELECT * FROM read_parquet('{input_path}')"

    # Execute the query and write the result to a CSV file
    conn.execute(f"COPY ({query}) TO '{output_path}' WITH HEADER")

    print(f"CSV file has been created at {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <input_path> <output_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    convert_parquet_to_csv(input_path, output_path)
