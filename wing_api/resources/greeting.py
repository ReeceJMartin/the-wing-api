import flask
from flask_restful import Resource, reqparse
import datetime


class Greeting(Resource):
    def get(self):
        file = open("currentMessage.txt", "r")

        message = file.read()

        file.close()

        messageJSON = {"message": message}

        return messageJSON, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("input", required=True)

        args = parser.parse_args()

        file = open("currentMessage.txt", "w")

        file.write(args["input"])

        file.close()

        # Make this more lightweight.
        time = datetime.datetime.now()

        inputJSON = {"input": [args["input"]], "time": [str(time)]}

        return inputJSON, 200

    pass
