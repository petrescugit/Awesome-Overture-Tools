#!/bin/bash

# Get the input directory and output directory as parameters
input_dir=$1
output_dir=$2

# Loop over all parquet files in the input directory
for input_file in "$input_dir"/*.parquet; do
    # Get the base name of the input file
    base_name=$(basename "$input_file" .parquet)
    
    # Construct the output file path
    output_file="$output_dir/$base_name.csv"

    # Call the Python script
    python3 convert.py "$input_file" "$output_file"
done
