#!/usr/bin/python3
"""the script fetches https://alx-intranet.hbtn.io/status URL"""
# fetch a URL
import urllib.request


if __name__ == "__main__":
    # get a URL
    url = 'https://intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        html = response.read()

    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content:{html.decode()}")
