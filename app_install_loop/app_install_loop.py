import os
import re
import time
import datetime
import requests

def write_timestamped_line(file, text):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write("{} - {}\n".format(timestamp, text))

package_name = "package_name"
application = "app_code"
apk_name = "apk_file_name"

url = "https://cp.pushwoosh.com/json/1.3/getTags"

# Id of the button from the layour inspector in AS
button_resource_id = "resource_id"

for i in range(3):
    # Install APK
    os.system('adb install C:/filepath/{}'.format(apk_name))

    time.sleep(10)

    # Launch app
    os.system('adb shell monkey -p {} 1'.format(package_name))

    # Wait for the app to load
    time.sleep(10)

    # Tap the button
    os.system('adb shell uiautomator dump')
    os.system('adb pull /sdcard/window_dump.xml C:/filepath/window_dump.xml')

    with open("C:/lama/window_dump.xml", "r") as file:
        xml_content = file.read()

    match = re.search(r'resource-id="{}.*?".*?bounds="(\[.*?\])"'.format(button_resource_id), xml_content, re.DOTALL)

    if match:
        button_bounds = match.group(1)
        coords = re.findall(r'\d+', button_bounds)
        x = (int(coords[0]) + int(coords[2])) // 2
        y = (int(coords[1]) + int(coords[3])) // 2
        os.system('adb shell input tap {} {}'.format(x, y))

    # Wait for 30 seconds
    time.sleep(30)


    # Get logs and search for HWID value
    logs = os.popen('adb logcat -d').read()
   
    with open("C:/filepath/logcat_logs.txt", "a") as f:
        f.write("Full Logcat Logs:\n")
        f.write(logs)
        f.write("\n\n")

    match = re.search(r'"hwid":"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})"', logs)

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

    # Send API request and log response
    response = requests.post(url, json=payload)
    with open("C:/filepath/api_log.txt", "a") as f:
        write_timestamped_line(f, "Request:")
        write_timestamped_line(f, str(payload))
        write_timestamped_line(f, "")
        write_timestamped_line(f, "Response:")
        write_timestamped_line(f, str(response.json()))
        write_timestamped_line(f, "")

    # Wait for 30 seconds
    time.sleep(30)

    # Uninstall app
    os.system('adb uninstall {}'.format(package_name))

    # Clear logs
    os.system('adb logcat -c')
