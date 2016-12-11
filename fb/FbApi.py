import requests
from flask import current_app

GRAPH_API = "https://graph.facebook.com/"

class FbApi:

    def __init__(self):
        self.version = "2.8"
        self.base_url = GRAPH_API
        self.access_token = current_app.config['FB_ACCESS_TOKEN']

    def get(self, path, **kwargs):
        params = {'access_token': self.access_token}
        params.update(**kwargs)

        response = requests.get(self.base_url + path, params = params)
        return response