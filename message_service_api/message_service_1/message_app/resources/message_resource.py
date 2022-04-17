from flask import request
from flask_restful import Resource, reqparse

from message_app.services.storage import Storage


class Message(Resource):
    storage = Storage()

    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        super(Message, self).__init__()

    def get(self):
        messages = self.storage.get_all()
        return messages, 200
