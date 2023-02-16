#!/bin/bash

# Set the API URL
url="https://cp.pushwoosh.com/json/1.3/getApplications"


key=$1

# Set the request data in JSON format
request='{"request": {"auth": "'$key'"}}'

# Execute the API request using curl and save the response to a variable
response=$(curl -s -H "Content-Type: application/json" -d "$request" $url 2> errors.log)

# Check the exit status of the curl command
if [ $? -ne 0 ]; then
  echo "An error occurred. See errors.log for details."
else
  # Print the response to the console
  echo $response

  # Save the response to a file
  echo $response > response.json
fi
