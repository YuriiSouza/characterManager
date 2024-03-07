def allCharacters():
    dataAllCharacter = []
    
    try:
        with open("dataCharacter.json", "r") as file:
            dataAllCharacter = file.read()
            
        return dataAllCharacter
    except:
        print("Não existem dados.")
        return dataAllCharacter
        
        


def saveCharacter(name, description, link, show, animator):
    character = {
        "name": str(name),
        "description": str(description),
        "link": str(link),
        "show": str(show),
        "animator": str(animator)
    }
    
    with open("dataCharacter.json", "a") as file:
        file.write(character)
        # file.write('{' + f'"name": "{name}","description":"{description}","link": "{link}","show": "{show}","animator":"{animator}"' + '},')
        