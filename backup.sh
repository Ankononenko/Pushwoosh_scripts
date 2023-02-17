#!/bin/bash

datetime=$1

# Create a backup directory
if [ ! -d "$(pwd)/backup" ]; then
    mkdir "$(pwd)/backup"
fi

if [ ! -d "$(pwd)/backup/${datetime}_backup" ]; then
    mkdir "$(pwd)/backup/${datetime}_backup"
fi

# Define the search pattern for the export segment files
search_pattern="export_segment_*_*.csv.zip"

# Loop through the files that match the search pattern and copy them to the backup directory
for file in $search_pattern; do
	cp $file $(pwd)/backup/${datetime}_backup
done

echo "export_segment files were copied to the backup folder"
