#!/usr/bin/python3
"""
This script fetches the status from a given URL using the requests package
and displays the response body.
"""

import requests


def fetch_status(url):
    """
    Fetches the status to the response body.
    """
    response = requests.get(url)
    body = response.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    fetch_status(url)
