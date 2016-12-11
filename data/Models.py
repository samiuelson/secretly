from datetime import datetime

from data.Db import db


class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    fbId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "User id %r" % self.id

class Tag(db.Model):

    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String, nullable=False, unique=True)
    enabled = db.Column(db.Boolean, default=True)

    def __init__(self, key, enabled):
        self.key = key
        self.enabled = enabled

    def __repr__(self):
        return "Tag %r" % self.key

class SentTag(db.Model):

    __tablename__ = "sent_tag"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)

    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sender = db.relationship('User', foreign_keys=[sender_id])

    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver = db.relationship('User', foreign_keys=[receiver_id])

    def __init__(self, sender, receiver, timestamp=None):
        self.sender = sender
        self.receiver = receiver
        if not timestamp:
            timestamp = datetime.utcnow()
        self.timestamp = timestamp

    def __repr__(self):
       return "Sent Tag"