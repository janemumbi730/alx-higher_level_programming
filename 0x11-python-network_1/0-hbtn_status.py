#!/usr/bin/python3
"""Fetch link provided from a host"""

if __name__ == '__main__':
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        content = response.read()

        decoded_content = content.decode("utf-8")

        print(f"Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {decoded_content}")
