import json


def nomValide(message):
    """
    List -> Bool
    message : liste contenant le nouveau nom saisie 
    Fonction qui vérifie si le nom du channel passé en argument est valide
    """
    # On vérifie si il y a un espace ou si aucun nom n'a été saisie
    if len(message) > 1 or len(message) < 1:
        return False
    for i in range(len(message[0])):
        # Renvoie faux si le charactère est un - ou un _ en dernière position
        if (message[0][i] == "-" or message[0][i] == "_") and (i == len(message[0])-1):
            return False
        # Sinon renvoie faux si le charactère est une majascule et si il s'agit d'un charactère spécial différent de - et _
        elif not((message[0][i].islower()) or message[0][i].isnumeric()) and not((message[0][i] == "-" or message[0][i] == "_")):
            return False
    # Renvoie vrai si tout les characters sont valide
    return True


# Fonction qui change le nom du channel sentiment dans le fichier "channel.json"


def setChannel(message, channel, channels):
    """ 
    Str X Str X Dict -> Str
    message : contenue du Message discord (le !setChannel) 
    channel : "general","accueil" ou "sentiment" en fonction de quel nom de salon à changer
    channels : dictionnaire contentant les noms des salons récupéré du channel.json 
    Fonction qui change le nom du channel sentiment dans le fichier "channel.json" si valide 
    """
    if nomValide(message.split()[1:]):
        # Change le nom du nouveau channel sentiment
        channels[channel] = message.split()[
            1].lower()
        # Met à jour fichier "channel.json"
        with open('channel.json', "w") as f:
            json.dump(channels, f)
        return "Le nouveau nom du channel " + channel + " est : "+channels[channel]
    else:
        if len(message.split()) == 1:
            return "!set"+channel.capitalize()+" doit être suivie d'un nom de salon valide (minuscule, sans espaces, sans caractères spéciaux sauf - et _ si il est suivi d'au moins un caractères)\nSalon "+channel+" actuel : "+channels[channel]
        else:
            return "!set"+channel.capitalize()+" doit être suivie d'un nom de salon valide (minuscule, sans espaces, sans caractères spéciaux sauf - et _ si il est suivi d'au moins un caractères)"
