import json

input_file = 'export_segment_4802D-434A7_1679044619.json'
output_filename = "output_devices_ne_date.csv"
num_devices_ne_date = 0

with open(input_file, 'r', encoding='utf-8') as f, open(output_filename, 'w', encoding='utf-8') as out_file:
    for line in f:
        data = json.loads(line)
        app_tags = data.get("app_tags", {})
        for app_key in app_tags:
            tags = app_tags[app_key].get("tags", [])
            for tag in tags:
                if tag["name"] == "First Install" and tag["date"] != "2021-11-18T00:00:00Z":
                    num_devices_ne_date += 1
                    out_file.write(line)
                    break
    out_file.write("\nTotal num of devices with not equal date,%d" % num_devices_ne_date)
