from app import db
from data.Models import Tag


def create_tags():
    tags = [
        Tag("coffee", True),
        Tag("go_dancing", True),
        Tag("have_a_drink", True),
        Tag("was_in_love", True),
        Tag("would_date", True),
        Tag("test", False)
    ]
    return tags


db.create_all()

for tag in create_tags():
    db.session.add(tag)

db.session.commit()