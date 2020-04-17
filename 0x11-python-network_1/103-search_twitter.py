#!/usr/bin/python3
"""Use the package request and connect to the twitter api"""
if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    import requests
    import sys
    import base64

    # Define your keys from the developer portal
    client_key = sys.argv[1]
    client_secret = sys.argv[2]
    # Reformat the keys and encode them
    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')

    # Transform from bytes to bytes that can be printed
    b64_encoded_key = base64.b64encode(key_secret)
    # Transform from bytes back into Unicode
    b64_encoded_key = b64_encoded_key.decode('ascii')

    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

    try:
        access_token = auth_resp.json()['access_token']
    except ValueError:
        print("Not a valid JSON")

    get_tweet = "{}1.1/search/tweets.json".format(base_url)
    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    parameters = {
        'q': sys.argv[3]
    }

    response = requests.get(get_tweet,
                            headers=search_headers, params=parameters)

    for i in range(5):
        id = response.json().get('statuses')[i].get('id')
        content = response.json().get('statuses')[i].get('text')
        owner = response.json().get('statuses')[i].get('user').get('name')

        print("[{}] {} by {}".format(id, content, owner))
