#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
displays the value of the X-Request-Id variable
found in the header of the response"""
import urllib.request
import sys

if __name__ == "__main__":
    # fetch the url
    url = sys.argv[1]
    
    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
    print(header)
