#!/usr/bin/python3
"""
This script fetches the status from a given URL using the requests package
and displays the response body.
"""

import requests
import sys

def fetch_status(url):
    """
    Fetches the status from the given URL and prints the type and content of the response body.
    """
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://alu-intranet.hbtn.io/status"
    fetch_status(url)
