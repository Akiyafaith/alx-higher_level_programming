#!/bin/bash
#  script that takes in a URL, sends a request to that URL,and display size

curl -s -w "%{size_download}" -o /dev/null "$1"
