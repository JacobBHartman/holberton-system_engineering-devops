#!/usr/bin/python3
'''
    This Python module contains a function that queries the Reddit API
    and returns the number of subscribers (not active users, total sub-
    scribers) for a given subreddit. If an invalid subreddit is given,
    the function should return 0.
'''


import requests

def number_of_subscribers(subreddit):
    '''
        This Python method queries the Reddit API
        and returns the number of subscribers (not active users, total sub-
        scribers) for a given subreddit. If an invalid subreddit is given,
        the function should return 0.
    '''
    header = {'User-Agent': 'Mozilla:1111:59.0.2'}
    url = "https://api.reddit.com"
    path = "/r/{}/about".format(subreddit)
    response = requests.get(url + path, headers=header)
    if response.status_code < 300:
        return response.json()['data']['subscribers']
    return 0
