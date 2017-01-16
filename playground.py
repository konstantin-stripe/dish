import requests
import json
import time
from os import environ

# from apikey import *

class ImageFetcher(object):

    def __init__(self):
        self.JSON_HEADER = {'content-type': 'application/json'}


        self.base_api = 'https://api.gettyimages.com'
        self.connect_api = 'https://connect.gettyimages.com'
        self.token_endpoint = 'oauth2/token'
        self.search_endpoint = 'v3/search/images'
        self.most_recent_token = None
        self.most_recent_token_time = 0

    def query(self, query_text):
        self._update_token()
        headers = {'Api-Key': environ.get('API_KEY'), 'Authorization': self.most_recent_token}
        payload = {'phrase': query_text}
        endpoint_url = '%s/%s' % (self.base_api, self.search_endpoint)
        response = requests.get(endpoint_url, payload, headers=headers)
        data = json.loads(response.text)
        if 'images' in data and len(data['images']) > 0:
            return data['images'][0]['display_sizes'][0]['uri']
        return None

    def _update_token(self):
        if not self.most_recent_token or time.time() - self.most_recent_token_time > 1500:
            # rerequest token
            payload = {'client_id': environ.get('API_KEY'), 'client_secret': environ.get('API_SECRET'), 'grant_type': 'client_credentials'}
            token_url = '%s/%s' % (self.connect_api, self.token_endpoint)
            response = requests.post(token_url, payload)
            if response.status_code == 200:
                data = json.loads(response.text)
                self.most_recent_token = data['access_token']
                self.most_recent_token_time = time.time()

i = ImageFetcher()
i.query('foo')
