from data import *

class Character():
    def __init__(self):
        # self.name = name
        # self.description = description
        # self.link = link
        # self.show = show
        # self.animator = animator
        try:
            self.name = str(input("Nome do personagem:"))
        except:
            print("Erro, nome não pode ser vazio.")
            
        try:
            self.description = str(input("Descrição: "))
        except:
            self.description = 'Sem descrição'
            
        try:
            self.link = str(input("Link da imagem: "))
        except:
            print("link não pode estar vazio.")
            
        try:
            self.show = str(input("Programa que o personagem aparece: "))
        except:
            print("Programa não pode estar vazio.")
            
        try:
            self.animator = str(input("Nome do animador: "))
        except:
            self.animator = "desconhecido"
    

    def save(self):
        try: 
            saveCharacter(self.name, self.description, self.link, self.show, self.animator)
            return True
        except:
            print("Erro ao salvar.")
            return False
        