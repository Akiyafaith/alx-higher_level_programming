#!/bin/bash
#  script that takes in a URL, sends a request to that URL,and display size
curl -s "$1" | wc -c
