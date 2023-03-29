import requests
import json
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed

ENDPOINT = "https://cp.pushwoosh.com/json/1.3"
API_KEY = "uQLLQR33nHOtGBbYIa25KmybcZZkliPWHmR1fjQ2zVU0FXZyfcChPmodNkB64XL8WcyNUUG5ix0c6DZRHM6n"
APP_CODE = "DB090-F69F7"
REGISTER_USER_URL = f"{ENDPOINT}/registerUser"

session = requests.Session()

def registerUser(hwid=None, userid=None):
    request = {
        "request": {
            "userId": userid,
            "auth": API_KEY,
            "hwid": hwid,
            "application": APP_CODE
        }
    }

    response = session.post(REGISTER_USER_URL, json=request)
    return response

def handle_result(future, hwid, userid, counter):
    try:
        r = future.result()
        print(f"Line: {counter}, HWID: {hwid}, UserID: {userid}, Response: {r.text}, Content: {r.content}")
    except Exception as e:
        print(f"Error: {e}")

with open("userID.csv", "r+") as f:
    rows = list(csv.reader(f, delimiter=',', quotechar='"'))

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(registerUser, hwid=row[0], userid=row[1]): (row[0], row[1], index + 1) for index, row in enumerate(rows)}

        for future in as_completed(futures):
            hwid, userid, counter = futures[future]
            handle_result(future, hwid, userid, counter)
            
        executor.shutdown(wait=True)
