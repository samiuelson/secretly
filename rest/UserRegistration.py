from flask_restful import Resource, reqparse

from fb.FbApi import FbApi


class UserRegistration(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('fb_access_token')
        self.fb_api = FbApi()


    ''' Sends user data in post request in order to register it '''
    def post(self):
        args = self.parser.parse_args()

        if 'fb_access_token' in args and args.get('fb_access_token'):
            fb_access_token = args.get('fb_access_token')
            params = {'input_token':fb_access_token}
            response = self.fb_api.get('/debug_token', **params)
            if response.status_code == 200:
                # TODO user access_token is valid
                # register user in db
                return "Success"
            else:
                return "Dude, you've sent bad access token", 401
        else:
            return "Nice try but... Not so easy! Didn't get fb_access_token param", 401


    ''' Checks if user is currently registered to Secretly backend '''
    def get(self):

        return "Nice try but... Not so easy!", 401