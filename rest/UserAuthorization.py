from flask_restful import Resource, reqparse

from fb.FbApi import FbApi


class UserAuthorization(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('fb_access_token')
        self.fb_api = FbApi()


    ''' Sends user data in post request in order to register it '''
    def post(self):
        args = self.parser.parse_args()

        if 'fb_access_token' in args and args.get('fb_access_token'):
            return "Success"
        else:
            return "Nice try but... Not so easy!", 401


    ''' Checks if user is currently registered to Secretly backend '''
    def get(self):

        return "Nice try but... Not so easy!", 401