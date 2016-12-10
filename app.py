from flask import Flask
from flask_restful import Api

from data.Db import db
from rest.TagsResource import TagsResource


def hello_world():
    return "Because I'm happy!"

def init_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    app.app_context().push()
    return app

app = init_app()

app.add_url_rule('/', view_func=hello_world)

api = Api(app)

api.add_resource(TagsResource, '/tags', endpoint='tags')

if __name__ == '__main__':
    app.run(debug=True)
