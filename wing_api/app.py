from flask import Flask
from flask_restful import Api
from wing_api.resources.greeting import Greeting

app = Flask(__name__)
api = Api(app)

api.add_resource(Greeting, "/greeting")


# Uncomment to use in Dev
# app.run(host='0.0.0.0', port=5001)

# Source to activate the venv
# gunicorn -w 4 'the-wing-api:app' used run the application with gunicorn
