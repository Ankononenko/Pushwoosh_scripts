import csv
import requests
from concurrent.futures import ThreadPoolExecutor

API_ENDPOINT = "https://cp.pushwoosh.com/json/1.3/deleteEmail"
HEADERS = {"Content-Type": "application/json"}

def send_request(hwid):
    payload = {
        "request": {
            "application": "737CE-E0304",
            "email": hwid
        }
    }
    response = requests.post(API_ENDPOINT, json=payload, headers=HEADERS)
    return response.json()

def process_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        hwids = [row['Hwid'] for row in csv_reader]

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(send_request, hwid) for hwid in hwids]
        for future in futures:
            print(future.result())

process_csv('segment_export_file.csv')
