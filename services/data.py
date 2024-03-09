def allCharacters():
    try:
        with open("dataCharacter.txt", "r") as file:
            lines = file.readlines()

        characters = []

        for line in lines:
            character = {}
            
            line = line.strip()
            
            fields = line.split(",")
            
            n = 0
            
            for field in fields:
                term = field.split(":")
                
                if n == 0:
                    character["name"] = term[1]
                elif n == 1:
                    character["description"] = term[1]
                elif n == 2:
                    character["link"] = term[1] + ':' + term[2]
                elif n == 3:
                    character["show"] = term[1]
                elif n == 4:
                    character["animator"] = term[1]
        
                n = n + 1
                    
            characters.append(character)
            
        return characters
    
    except:
        print("Não existem dados.")
        return []


def saveCharacter(name, description, link, show, animator):
    character = {
        "name": str(name),
        "description": str(description),
        "link": str(link),
        "show": str(show),
        "animator": str(animator)
    }
    
    with open("dataCharacter.txt", "a") as file:
        file.write('{' + f'"name":{name},"description":{description},"link":"{link}","show":{show},"animator":{animator}' + '}\n')
        