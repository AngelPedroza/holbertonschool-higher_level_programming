#!/usr/bin/python3
"""Use the package request and connect to the github api"""
if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    import requests
    import sys

    repo = sys.argv[1]
    user = sys.argv[2]

    r = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(user, repo)
    )


    data = r.json()
    #find the sha and enter to the commit dic
    for dic in data[:10]:
        for sha_key, sha_value in dic.items():
            if sha_key == "sha":
                sha = sha_value
            if sha_key == "commit":
                    print("{}: {}".format(sha, sha_value['author'].get('name')))
