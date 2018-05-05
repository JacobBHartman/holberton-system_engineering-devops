#!/usr/bin/python3
'''
    This Python module contains a function that queries the Reddit API
    and prints the titles of the first 10 hot posts listed for a given
    subreddit
'''


import requests


def top_ten(subreddit):
    '''
        This Python method queries the Reddit API
        and prints the titles of the first 10 hot posts listed for a given
        subreddit
    '''
    header = {'User-Agent': 'Mozilla:1111:59.0.2'}
    url = "https://api.reddit.com"
    path = "/r/{}/hot/".format(subreddit)
    response = requests.get(url + path, headers=header, allow_redirects=False)
    if response.status_code < 300:
        for i in range(10):
            if response.json()['data']['children'][i]['data']['title']:
                print(response.json()['data']['children'][i]['data']['title'])
    print(None)
