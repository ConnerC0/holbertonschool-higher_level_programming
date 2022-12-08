#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays the
value of the variable X-Request-Id in the response header"""

from sys import argv
import requests


if __name__ == "__main__":
    request = requests.get(argv[1])

    print(request.headers.get('X-Request-Id'))