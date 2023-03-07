import os
import fnmatch

folder_path = 'Folder_path'
num_lines = 0

for filename in fnmatch.filter(os.listdir(folder_path), '*.csv'):
    file_path = os.path.join(folder_path, filename)
    with open(file_path, encoding='utf-8') as f:
        for i, line in enumerate(f):
            pass
    num_lines += i + 1
    print(f"{filename}: {i+1} lines")

print(f"Total lines: {num_lines}")
