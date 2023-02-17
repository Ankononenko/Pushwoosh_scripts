#!/bin/bash

# Define the search pattern for the export segment files
search_pattern="export_segment_*_*.csv.zip"

# Loop through the files that match the search pattern
for file in $search_pattern; do
  # Extract the app code from the file name
  app_code=$(echo $file | sed 's/export_segment_\(.*\)_.*/\1/')

  # Extract the file ending from the file name
  file_ending=$(echo $file | sed 's/.*_\([0-9]*\.csv\)/_\1/')

  # Generate the command and write it to the output file
  echo "./process-segment --token ${key} -a deleteDevice --app ${app_code} ${file}" >> process_requests.sh
done

echo "File with list of process requets was generated: process_requets.sh"
