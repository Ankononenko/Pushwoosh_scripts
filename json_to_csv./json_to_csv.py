import json
import pandas as pd

input_file = 'output_devices_ne_date.json'  # Change this to the name of your input file
output_filename = "output_devices_final.csv"

data_list = []

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)

        device_info = {}
        device_info['hwid'] = data['hwid']

        # Process device_tags
        for tag in data.get("device_tags", []):
            device_info[tag["name"]] = tag.get("integer") or tag.get("date") or tag.get("string") or tag.get("boolean") or tag.get("version") or tag.get("timezone")

        # Process app_tags
        app_tags = data.get("app_tags", {})
        for app_key in app_tags:
            tags = app_tags[app_key].get("tags", [])
            for tag in tags:
                device_info[tag["name"]] = tag.get("integer") or tag.get("date") or tag.get("string") or tag.get("boolean") or tag.get("version") or tag.get("timezone")

        data_list.append(device_info)

df = pd.DataFrame(data_list)
df.to_csv(output_filename, index=False, encoding='utf-8')
