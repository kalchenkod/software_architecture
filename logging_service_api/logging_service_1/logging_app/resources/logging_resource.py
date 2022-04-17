from flask_restful import Resource, reqparse

from logging_app.services.storage_service import Storage


class Logging(Resource):
    storage = Storage()

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("uuid", type=int, location="json")
        self.reqparse.add_argument("msg", type=str, location="json")

        super(Logging, self).__init__()

    def get(self):
        return self.storage.get_all(), 200

    def post(self):
        args = self.reqparse.parse_args()

        message = args['msg']
        uuid = args['uuid']
        print(message)

        self.storage.store(uuid=uuid, message=message)
        return 200
