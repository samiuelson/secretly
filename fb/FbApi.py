from flask import current_app

GRAPH_API = "https://graph.facebook.com/"

class FbApi:

    def __init__(self):
        self.version = "2.8"
        self.base_url = GRAPH_API
        access_token = current_app.config['FB_ACCESS_TOKEN']