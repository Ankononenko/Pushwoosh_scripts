#!/bin/bash

authToken="key"
appCodesFile="app_codes.txt"
responseLogFile="response_log.txt"

# Clear the log file at the beginning
> "$responseLogFile"

# Loop through each line in the file
while IFS= read -r appCode; do
    payload=$(cat <<EOF
{
  "request": {
    "auth": "$authToken",
    "application": "$appCode"
  }
}
EOF
)

    response=$(curl -X POST -H "Content-Type: application/json" -d "$payload" "https://api.pushwoosh.com/json/1.3/deleteApplication")

    echo "Response for $appCode: $response"
    echo "Response for $appCode: $response" >> "$responseLogFile"
done < "$appCodesFile"

echo "Responses have been logged in $responseLogFile."
