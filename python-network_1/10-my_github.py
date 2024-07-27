#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's id.
"""


import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    print(response.json().get("id"))
