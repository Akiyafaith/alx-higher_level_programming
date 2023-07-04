"""the script fetches https://alx-intranet.hbtn.io/status"""
#!/usr/bin/python3
# fetch a URL
import urllib.request


if __name__ == "__main__":
url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()
print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode('utf-8'))
