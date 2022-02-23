from flask import Flask
from flask_restful import Api, reqparse, Resource


from facade_app.resources.facade_resource import Facade


app = Flask(__name__)
api = Api(app)


api.add_resource(Facade, "/facade")

if __name__ == '__main__':
    app.run(port=5054)
