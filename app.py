from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def hello_world():
    return "Because I'm happy!"


def init_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.add_url_rule('/', view_func=hello_world)
    app.app_context().push()
    return app

app = init_app()
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()
