from flask import Flask, request
from services.character import *
from services.data import *
# from flask_restplus import Api, Resource


app = Flask(__name__)
# api = Api(app)

@app.route('/')
def serverWorks():
    return 'work'

@app.route("/characters")
def showCharactersAPI():
    data = allCharacters()
        
    return data

@app.post('/character')
def createCharacter():
    data = request.get_json()
    # {
    #     {
    #         "name":"Gwen Stacy",
    #         "description":"Gosta do Milles Morales",
    #         "link":"https://upload.wikimedia.org/wikipedia/pt/5/52/Mulher-Aranha_%28Gwen_Stacy%29_em_Aranhaverso_2.png",
    #         "show": "Aranhaverso",
    #         "animator": "desconhecido"
    #     }
    # }
    
    name = data['name']
    description = data['description']
    link = data['link']
    show = data['show']
    animator = data['animator']
    
    character = Character(name, description, link, show, animator)
    character.save()
    
    res = f'''{ character.name }
    { character.description }
    { character.animator }
    { character.link }
    { character.show }
    { character.animator }'''
    
    return res
