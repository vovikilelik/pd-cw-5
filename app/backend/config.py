from flask import Flask
from flask_restx import Api

app = Flask('__name__', template_folder='./html/templates', static_folder='./html/static')

app_api = Api(app)
