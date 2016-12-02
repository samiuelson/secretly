from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()


@app.route('/')
def hello_world():
    return "Because I'm happy!"


if __name__ == '__main__':
    app.run()
