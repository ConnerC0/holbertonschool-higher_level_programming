#!/usr/bin/python3
"""a Python script that fetches https://intranet.hbtn.io/status"""

import requests


if __name__ == "__main__":
    request = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {_type}'.format(_type=type(request.text)))
    print('\t- content: {_content}'.format(_content=request.text))
