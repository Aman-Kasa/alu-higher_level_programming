#!/usr/bin/python3
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Check if the file exists and load existing items if it does
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add command line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
