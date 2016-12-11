from flask_restful import Resource, marshal_with, fields

from data.Models import Tag

class TagsResource(Resource):

    tag_fields = {
        'id': fields.Integer,
        'key': fields.String,
    }

    @marshal_with(tag_fields)
    def get(self):
        return Tag.query.filter_by(enabled = True).all()