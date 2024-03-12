from flask import Flask
from flask_restx import Api, Resource
from services.database import *

class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app, 
            version='1.0', 
            title='API character manager',
            description='API para gerenciar personagens.', 
            doc='/'
        )
        
    def run(self):
        self.app.run(
                debug=True,
            )
        database.initDb()

server = Server()
