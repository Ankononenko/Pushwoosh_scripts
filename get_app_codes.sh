#!/bin/bash

# Set the API URL
url="https://cp.pushwoosh.com/json/1.3/getApplications"

# Set the input variable
key=$1

# Set the request data in JSON format
request='{"request": {"auth": "'$key'"}}'

# Get current time and date in a format suitable for a file name
datetime=$2

# Execute the API request using curl and save the response to a variable
response=$(curl -s -H "Content-Type: application/json" -d "$request" $url 2> errors_${datetime}.log) 

# Check the exit status of the curl command
if [ $? -ne 0 ]; then
  echo "An error occurred. See errors_${datetime}.log for details."
else
  # Print the response to the console
  echo $response
  echo "The output of the request was written to the reponse_${datetime}.json file in this folder"
  
  # Save the response to a file
  echo $response > response_${datetime}.json
fi
