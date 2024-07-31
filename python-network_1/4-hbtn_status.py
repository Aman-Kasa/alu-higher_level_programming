#!/usr/bin/python3
"""
This script fetches https://alu-intranet.hbtn.io/status
using the requests package and displays the response body.
"""

import requests

def fetch_status():
    """
    Fetches the status from https://alu-intranet.hbtn.io/status
    and prints the type and content of the response body.
    """
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))

if __name__ == "__main__":
    fetch_status()
