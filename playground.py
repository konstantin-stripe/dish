import requests

from apikey import *

base_api = 'https://api.gettyimages.com'
connect_api = 'https://connect.gettyimages.com'
token_endpoint = 'oauth2/token'
search_endpoint = '/v3/seach/images'
most_recent_token = None
most_recent_token_time = 0

def get_image_url(query_text):
    if not most_recent_token or time.time() - most_recent_token_time > 1500:
        # rerequest token
        payload = {'client_id': getty_api_key, 'client_secret': getty_api_secret, 'grant_type': 'client_credentials'}
        token_url = '/'.join([connect_api, token_endpoint])
        print token_url
        response = requests.post(token_url, params=payload)
        print response.text
    else:
        pass

get_image_url('foo')
