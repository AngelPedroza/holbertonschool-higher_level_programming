#!/usr/bin/python3
"""Use the package request"""
if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 1:
        dic = {'q': ""}
    else:
        dic = {'q': sys.argv[1]}

    r = requests.post('http://0.0.0.0:5000/search_user', data=dic)
    try:
        data = r.json()
        if data:
            print("{} {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
