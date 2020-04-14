#!/usr/bin/python3
"""Send a POST"""
if __name__ == "__main__":
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            li = str(response.read())
            print(li)
            print(response.read())
    except urllib.error.HTTPError as error:
            print("Error code: {}".format(error.code))
