#!/usr/bin/python3
"""send a POST request"""

if __name__ == '__main__':
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"

    try:
        q = sys.argv[1]

    except IndexError:
        q = ""

    variables = {'q': q}

    with requests.post(url, data=variables) as response:
        try:
            content = response.json()

            if len(content) != 0:
                print(f"[{content.get('id')}] {content.get('name')}")
            else:
                print("No result")

        except Exception:
            print("Not a valid JSON")
