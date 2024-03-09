from services.character import *
from services.data import *

def showCharacters():
    data = allCharacters()
    for character in data:
        print("Name:", character["name"])
        print("Description:", character["description"])
        print("Link:", character["link"])
        print("Show:", character["show"])
        print("Animator:", character["animator"])
        print("-" * 30)
        
        
    return data


def main():
    print('''
    

  /$$$$$$                                                    /$$                 /$$                                 /$$          
 /$$__  $$                                                  |__/                | $$                                | $$          
| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$ /$$  /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$         /$$$$$$$  /$$$$$$ 
| $$ /$$$$ /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$ /$$_____/| $$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$       /$$__  $$ /$$__  $$
| $$|_  $$| $$$$$$$$| $$  \__/| $$$$$$$$| $$  \ $$| $$      | $$  /$$$$$$$| $$  | $$| $$  \ $$| $$  \__/      | $$  | $$| $$$$$$$$
| $$  \ $$| $$_____/| $$      | $$_____/| $$  | $$| $$      | $$ /$$__  $$| $$  | $$| $$  | $$| $$            | $$  | $$| $$_____/
|  $$$$$$/|  $$$$$$$| $$      |  $$$$$$$| $$  | $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$            |  $$$$$$$|  $$$$$$$
 \______/  \_______/|__/       \_______/|__/  |__/ \_______/|__/ \_______/ \_______/ \______/ |__/             \_______/ \_______/
                                                                                                                                  
                                                                                                                                  
                                                                                                                                  
 /$$$$$$$                                                                                                                         
| $$__  $$                                                                                                                        
| $$  \ $$ /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$                     
| $$$$$$$//$$__  $$ /$$__  $$ /$$_____/ /$$__  $$| $$__  $$ |____  $$ /$$__  $$ /$$__  $$| $$__  $$ /$$_____/                     
| $$____/| $$$$$$$$| $$  \__/|  $$$$$$ | $$  \ $$| $$  \ $$  /$$$$$$$| $$  \ $$| $$$$$$$$| $$  \ $$|  $$$$$$                      
| $$     | $$_____/| $$       \____  $$| $$  | $$| $$  | $$ /$$__  $$| $$  | $$| $$_____/| $$  | $$ \____  $$                     
| $$     |  $$$$$$$| $$       /$$$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$  | $$ /$$$$$$$/                     
|__/      \_______/|__/      |_______/  \______/ |__/  |__/ \_______/ \____  $$ \_______/|__/  |__/|_______/                      
                                                                      /$$  \ $$                                                   
                                                                     |  $$$$$$/                                                   
                                                                      \______/                                                    

                                                 
''')

    while True:
        #Selection menu
        # 1 - Ver personagens
        # 2 - Criar personagem
        # 3 - Fechar gerenciador
        while True:
            try:
                action = int(input('1 - Ver personagens\n2 - Criar personagem\n3 - Fechar gerenciador\n'))
            except:
                print("Error, insira um valor")
                
            if action == 1 or action == 2 or action == 3:
                break
            else:
                print("Erro, opção inserida não suportada.")
        
            
            if action == 1:
                showCharacters()
            elif action == 2:
                try:
                    name = str(input("Nome do personagem:"))
                except:
                    print("Erro, nome não pode ser vazio.")
                    
                try:
                    description = str(input("Descrição: "))
                except:
                    description = 'Sem descrição'
                    
                try:
                    link = str(input("Link da imagem: "))
                except:
                    print("link não pode estar vazio.")
                    
                try:
                    show = str(input("Programa que o personagem aparece: "))
                except:
                    print("Programa não pode estar vazio.")
                    
                try:
                    animator = str(input("Nome do animador: "))
                    if animator == '':
                        animator = 'desconhecido'
                except:
                    animator = "desconhecido"
        
            character = Character(name, description, link, show, animator)
            
            character.save()
            
        else:
            break
            
            
if __name__ == '__main__':
    main()
    