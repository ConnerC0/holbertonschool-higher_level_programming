#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays 
the body of the response (decoded in utf-8)."""

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError


if __name__ == "__main__":
    request = Request(argv[1])

    try:
        with urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as exception:
        print('Error code:', exception.code)
