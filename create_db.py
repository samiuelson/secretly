from app import db
from data.Models import Tag

def create_tag():
    t = Tag("coffee", True)
    return t


db.create_all()

db.session.add(create_tag())

db.session.commit()