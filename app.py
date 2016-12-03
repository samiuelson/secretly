from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def hello_world():
    return "Because I'm happy!"

db = SQLAlchemy()

def init_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.add_url_rule('/', view_func=hello_world)
    app.app_context().push()
    db.init_app(app)
    app.app_context().push()

    return app

app = init_app()

if __name__ == '__main__':
    app.run()
