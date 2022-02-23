from flask import request
from flask_restful import Resource, reqparse

from message_app.services.static_response_service import StaticResponse


class Message(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

        super(Message, self).__init__()

    def get(self):
        static_response = StaticResponse.get_static_response()
        return static_response, 200
