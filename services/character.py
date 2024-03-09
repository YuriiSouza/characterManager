from services.data import *

class Character():
    def __init__(self, name, description, link, show, animator):
        self.name = name
        self.description = description
        self.link = link
        self.show = show
        self.animator = animator


    def save(self):
        try: 
            saveCharacter(self.name, self.description, self.link, self.show, self.animator)
            return True
        except:
            print("Erro ao salvar.")
            return False
        