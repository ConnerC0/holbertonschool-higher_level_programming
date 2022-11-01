#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''

    site = 'http://0.0.0.0:5000/search_user'
    request = requests.post(site, data={'q': q}).json()
    try:
        if {'id', 'name'} <= request.keys():
            print('[{id}] {name}'.format(id=request.get('id'), name=request.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')

