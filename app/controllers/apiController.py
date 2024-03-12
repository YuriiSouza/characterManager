from flask import request
from flask_restx import Resource, Namespace, fields
from uuid import uuid4

from server.instance import server
from services.manager import *

api = server.api

# Defining the namespace for characters
characters_ns = Namespace('characters', description='Character-related operations')

# Defining the input model to create a character
character_model = api.model('Character', {
    'name': fields.String(required=True, description='Character`s Name'),
    'description': fields.String(required=True, description='Character description'),
    'link': fields.String(required=True, description='Link to character image'),
    'show': fields.String(required=True, description='Name of the program in which the character appears'),
    'animator': fields.String(required=True, description='Name of the animator responsible for the character')
})

@api.route("/characters")
class CharacterApi(Resource):
    
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self):
        """
        Returns all characters.
        """
        data = Characters.select()
        
        return data


    @api.doc(responses={201: 'Created', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(character_model)
    def post(self):
        """
        Create a new character.        
        """
        data = request.get_json()
        
        name = data.get('name')
        description = data.get('description')
        link = data.get('link')
        show = data.get('show')
        animator = data.get('animator')
        
        character = Characters(name=name, description=description, link=link, show=show, animator=animator)
        character.save()
        
        return {'message': 'Character created successfully'}, 201