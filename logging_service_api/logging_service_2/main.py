from flask import Flask
from flask_restful import Api, reqparse, Resource


from logging_app.resources.logging_resource import Logging


app = Flask(__name__)
api = Api(app)


api.add_resource(Logging, "/logging")

if __name__ == '__main__':
    app.run(port=5057)
