import os
import re
import time
import requests

package_name = "com.example.app"
application = "YOUR_HWID_GOES_HERE"
apk_name = "YOUR_APK_NAME_GOES_HERE.apk"

url = "API_REQUEST_URL"

num_loops = 3

for i in range(num_loops):
    # Install the APK
    os.system('adb install /storage/emulated/0/Download/{}'.format(apk_name))

    # Launch the app
    os.system('adb shell monkey -p {} 1'.format(package_name))

    # Wait for 2 minutes
    time.sleep(120)

    # Get logs and search for HWID value
    logs = os.popen('adb logcat -d').read()
    match = re.search(r"HWID: ([0-9a-fA-F-]+)", logs)
    if match:
        hwid = match.group(1)
    else:
        hwid = ""

    payload = {
    "request":{
        "application": application,
        "hwid": hwid
    }
    }

    # Send an API request and log the response
    response = requests.post(url, json=payload)
    with open("/storage/emulated/0/api_log.txt", "a") as f:
        f.write("Request:\n")
        f.write(str(payload))
        f.write("\n\n")
        f.write("Response:\n")
        f.write(str(response.json()))
        f.write("\n\n")

    # Wait for 30 seconds
    time.sleep(30)

    # Uninstall app
    os.system('adb uninstall {}'.format(package_name))

    # Clear logs so we can parse a new HWID
    os.system('adb logcat -c')
