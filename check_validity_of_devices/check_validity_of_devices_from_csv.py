import requests
import csv
import time
import json
 
def read_tokens(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        tokens = list(reader)
    # skip the header
    return tokens[1:]
 
def send_request(tokens):
    url = "https://cp.pushwoosh.com/json/1.3/createMessage"
    headers = {'Content-Type': 'application/json'}
    data = {
        "request": {
            "application": "APP_CODE",
            "auth": "TOKEN",
            "notifications": [
                {
                    "send_date": "now",
                    "ignore_user_timezone": True,
                    "content": "test",
                    "devices": tokens,
                    # Enter the needed platforms and edit the silent options according to the documentation:
                    # https://docs.pushwoosh.com/platform-docs/api-reference/messages
                    "platforms": [1, 3],
                    "ios_silent": 1,
                    "android_silent": 1
                }
            ]
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()
 
def main():
    tokens = read_tokens("tokens.csv")
    unknown_tokens = []
    for i in range(0, len(tokens), 1000):
        chunk = tokens[i:i+1000]
        chunk = [item[0] for item in chunk]  # take the token from the row
        response = send_request(chunk)
        if 'UnknownDevices' in response['response']:
            unknown_devices = list(response['response']['UnknownDevices'].values())[0]
            unknown_tokens.extend(unknown_devices)
        time.sleep(1)  # to avoid potential rate limiting
    with open('unknown_tokens.csv', 'w') as f:
        writer = csv.writer(f)
        for token in unknown_tokens:
            writer.writerow([token])
    print(f"Number of unknown devices: {len(unknown_tokens)}")
 
if __name__ == "__main__":
    main()
