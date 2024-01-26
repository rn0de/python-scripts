import os
from pathlib import Path

def rename_files(start_path, old_prefix, new_prefix):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.startswith(old_prefix):
                old_file = Path(root) / file
                new_file = Path(root) / file.replace(old_prefix, new_prefix, 1)
                os.rename(old_file, new_file)
                print(f"Renamed '{old_file}' to '{new_file}'")


start_directory = '/path/to/your/directory' 
old_prefix = 'Products_'
new_prefix = 'produ_'

rename_files(start_directory, old_prefix, new_prefix)
