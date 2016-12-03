from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fbId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "User id %r" % self.id

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    key = db.Column(db.String, nullable=False)
    enabled = db.Column(db.Boolean, default=True)

    def __init__(self, key, enabled):
        self.key = key
        self.enabled = enabled

    def __repr__(self):
        return "Tag %r" % self.key

class SentTag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime)

    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sender = db.relationship('User')

    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver = db.relationship('User')

    def __init__(self, sender, receiver, timestamp=None):
        self.sender = sender
        self.receiver = receiver
        if not timestamp:
            timestamp = datetime.utcnow()
        self.timestamp = timestamp

    def __repr__(self):
       return "Sent Tag"