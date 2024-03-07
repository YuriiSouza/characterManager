#!/usr/bin/env python3

from character import *
from data import *


#formatar output melhor futuramente
def showCharacters():
    data = allCharacters()
    for character in data:
        print("Name:", character["name"])
        print("Description:", character["description"])
        print("Link:", character["link"])
        print("Show:", character["show"])
        print("Animator:", character["animator"])
        print("-" * 30)
        
    


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
            character = Character()
            
            character.save()
            
        else:
            break
            
            
if __name__ == '__main__':
    main()
    