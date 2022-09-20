#!/usr/bin/python3
""" task 7 load, add, save """
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
from sys import argv

filename = "add_item.json"

try:
    jsonList = load_from_json_file(filename)
except:
    jsonList = []
save_to_json_file(jsonList + argv[1:], filename)
