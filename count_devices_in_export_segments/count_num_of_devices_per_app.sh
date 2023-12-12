#!/bin/bash

outputFile="num_of_devices_per_app.txt"

> "$outputFile"

for file in *.csv; do
    appCode=$(echo "$file" | sed -E 's/export_segment_([^_]+)_.+/\1/')
    numLines=$(( $(wc -l < "$file") - 1 ))
    echo "$appCode - $numLines" >> "$outputFile"
done

echo "Data has been written to $outputFile."
