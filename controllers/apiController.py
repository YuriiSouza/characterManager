from flask import request
from flask_restx import Resource, Namespace, fields

from server.instance import server
from services.character import *

api = server.api

# Definindo o namespace para os personagens
characters_ns = Namespace('characters', description='Operações relacionadas aos personagens')

# Definindo o modelo de entrada para criar um personagem
character_model = api.model('Character', {
    'name': fields.String(required=True, description='Nome do personagem'),
    'description': fields.String(required=True, description='Descrição do personagem'),
    'link': fields.String(required=True, description='Link para a imagem do personagem'),
    'show': fields.String(required=True, description='Nome do programa em que o personagem aparece'),
    'animator': fields.String(required=True, description='Nome do animador responsável pelo personagem')
})

@api.route("/characters")
class Characters(Resource):
    
    @api.doc(responses={200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    def get(self):
        """
        Retorna todos os personagens.
        """
        data = allCharacters()
        return data

    @api.doc(responses={201: 'Created', 400: 'Invalid Argument', 500: 'Mapping Key Error'})
    @api.expect(character_model)
    def post(self):
        """
        Cria um novo personagem.
        """
        data = request.get_json()
        
        name = data['name']
        description = data['description']
    
        if 'https://' not in data['description']:
            return { 'message': 'Link não aceito, https:// requirido'}, 400
        
        link = data['link']
        show = data['show']
        animator = data['animator']
        
        character = Character(name, description, link, show, animator)
        character.save()
        
        return {'message': 'Personagem criado com sucesso'}, 201
