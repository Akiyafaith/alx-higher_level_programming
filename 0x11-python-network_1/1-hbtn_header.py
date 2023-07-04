#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
displays the value of the X-Request-Id variable
found in the header of the response"""
import urllib.request
import sys

if ___name__ = "__main__":
    # fetch the url
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.headers

    request_id = headers.get('X-Request-Id')
    print(request_id)
