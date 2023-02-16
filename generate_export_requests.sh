#!/bin/bash

# read in response.json and extract app codes
app_codes=$(jq -r '.response.applications | keys | .[]' response.json)

# loop through app codes and execute export-segment command
for code in $app_codes
do
    cmd="./export-segment --token yh9JPlJQkYpruy36TUU81pK6T5QLSRgoNl1ftvPHRw234ELm5TfWwzcCnntan6LHENeA0StenAHKpsoAwWZR 'AT(\"${code}\",\"Last Application Open\", GTE, \"180 days ago\")'"
    echo $cmd >> export_requests.sh
done
