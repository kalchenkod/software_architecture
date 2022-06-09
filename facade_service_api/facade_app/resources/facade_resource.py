from flask import request
from flask_restful import Resource, reqparse

from facade_app.services.uuid_generation_service import UUIDGeneration
from facade_app.services.logging_service import Logging
from facade_app.services.messaging_service import Messaging


class Facade(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("msg", location="json")

        self.logging = Logging()
        self.messaging = Messaging()

        super(Facade, self).__init__()

    def get(self):
        messaging_service_messages = self.messaging.get_messages()
        logging_service_messages = self.logging.get_messages()

        response = f"Messaging: {messaging_service_messages} \n Logging: {logging_service_messages}"
        print(response)
        return response, 200

    def post(self):
        args = self.reqparse.parse_args()
        message = args['msg']
        uuid = UUIDGeneration.generate_uuid()

        response = self.messaging.write_to_queue(msg=message)
        response = self.logging.log(uuid=uuid, message=message)
        return response, 200
