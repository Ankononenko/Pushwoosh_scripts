#!/bin/bash

echo "Do you want to delete the temporary files?(Y/n)"
read input

if [ "$input" = "Y" ] || [ "$input" = "y" ]; then
    find . -type f -name 'response_*_*.json' -delete
    find . -type f -name 'export_requests_*_*.sh' -delete
    find . -type f -name 'process_requests_*_*.sh' -delete
    find . -type f -name 'errors_*_*.log' -delete
    rm *.csv
    rm *.zip
else
    echo "Not deleting any files."
fi

