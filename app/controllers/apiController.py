from flask import request
from flask_restx import Resource, Namespace, fields
from uuid import uuid4
from peewee import *

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
class CharactersApi(Resource):
    
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self):
        """
        Returns all characters.
        """
        query = Characters.select()
        results_dict = []
        
        for character in query:
            character_dict = {
                'id': str(character.id),
                'name': character.name,
                'description': character.description,
                'link': character.link,
                'show': character.show,
                'animator': character.animator
            }
            results_dict.append(character_dict)

        
        return results_dict


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
        
        try:
            character = Characters.create(name=name, description=description, link=link, show=show, animator=animator)
            
            
            return {'message': 'Character created'}, 201
        except:
            return { 'message': 'Character not created'}, 400
        

     
@api.route("/character/<string:id>")
class character(Resource):
    
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.doc(params={'id': 'An ID'})
    @api.expect(id)
    def get(self, id):
        """
        Get a specific character.
        """
        character = Characters.get(Characters.id == id)
        
        character_dict = {
            'id': str(character.id),
            'name': character.name,
            'description': character.description,
            'link': character.link,
            'show': character.show,
            'animator': character.animator
        }

        
        return character_dict
    
    
    @api.doc(responses={ 200: 'updated', 400: 'Invalid Argument', 500: 'Mapping Key Error', 600: 'Character doesnt exists.'})
    @api.doc(params={'id': 'An ID'})
    @api.expect(character_model, id)
    def put(self, id):
        """
        Upgrade a specific character.
        """
        
        try:
            data = request.get_json()
        
            name = data.get('name')
            description = data.get('description')
            link = data.get('link')
            show = data.get('show')
            animator = data.get('animator')
            
            try:
                character = Characters.get(Characters.id == id)
                
                character.name = name
                character.description = description
                character.link = link
                character.show = show
                character.animator = animator
                
                character.save()
                
                return 201
                
            except:
                return 600
            
        except:
            return 400
        
        # character.
        
        

    @api.doc(responses={ 200: 'deleted', 400: 'Invalid', 500: 'Mapping Key Error'})
    @api.doc(params={'id': 'An ID'})
    @api.expect(id)
    def delete(self, id=None):
        """
        Delete a specific character.
        """
        try:
            character = Characters.get(Characters.id == id)
            character.delete_instance()
            
            return 200
        except:
            return 400
        
        
        