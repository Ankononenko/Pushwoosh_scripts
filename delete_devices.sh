#!/bin/bash

echo "Please enter the API key for the apps that you want to extract"

read key

./get_app_codes.sh $key
./generate_export_requests.sh
