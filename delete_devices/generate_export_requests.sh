#!/bin/bash

# Date and time for file title
datetime=$2

# Read in response.json and extract app codes
app_codes=$(jq -r '.response.applications | keys | .[]' response_${datetime}.json)
key=$1

# Loop through app codes and execute export-segment command
for code in $app_codes
do
    cmd="./export-segment --token ${key} 'AT(\"${code}\",\"Last Application Open\", GTE, \"30 days ago\")'"
    echo $cmd >> export_requests_${datetime}.sh
done
echo "The export requests were written to the export_requests_${datetime}.sh file"
