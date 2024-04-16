#!/usr/bin/python3
"""
This script loads existing items from a JSON file, adds any command line
arguments provided when running the script, and saves the updated list
to a file in JSON format.
"""

import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

items = []

try:
    items = load_from_json_file("add_item.json")
except Exception:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")
