# https://www.youtube.com/watch?v=Vz67oGgdXoQ&t=2075s&ab_channel=SohanPy

import discord

color = discord.Color.dark_blue()
error_color = discord.Color.red()

emoji = "\U0001F613"

# Dictionnaire des mots remplacés
key_features = {
    'temp': 'Temperature',
    'feels_like': 'Ressenti',
    'temp_min': 'Temperature minimum',
    'temp_max': 'Temperature maximum'
}


def parse_data(data):
    """
    Dict -> Dict
    data : format json du contenu de l'url
    Fonction permettant de faire le tri sur ce que l'on veut
    Dans ce cas là humidity et pressure sont supprimer
    """
    del data['humidity']
    del data['pressure']
    return data

# Fonction affichant tout ce qui est nécessaire


def weather_message(data, localisation):
    """
    Dict x String -> Embed
    data : dictionnaire de la variable que renvoit la fonction parse_data
    localisation : chaine de caractère tapé après !meteo
    Fonction qui renvoit toutes les données nécessaires en forme d'embed
    """
    localisation = localisation.title()
    # message contient titre et couleur
    message = discord.Embed(
        title=f'Meteo de {localisation}',
        color=color
    )
    message.set_thumbnail(
        url='https://image.winudf.com/v2/image1/b3JnLmFuZHJvd29ya3Mua2xhcmFfaWNvbl8xNjExMzc2NDc2XzAzMQ/icon.png?w=&fakeurl=1')
    # Parcours les clé dans data
    for key in data:
        # Ajoute un champ dans message
        message.add_field(
            name=key_features[key],
            value=f'{str(data[key])}°C',
            inline=False
        )

    return message

# Fonction lors d'un erreur


def error_message(localisation):
    """
    String -> Embed
    localisation : chaine de caractère tapé après !meteo
    Fonction qui indique lorsque la commande a été mal formulé
    """
    localisation = localisation.title()
    return discord.Embed(
        title='Error',
        description=f'Mille excuses mais je ne peux pas trouver la météo d’une ville qui n’existe pas !{emoji}  ',
        color=error_color
    )


def only_meteo():
    """
    None -> Embed
    Fonction qui indique lorsque la commande a été mal formulé
    """
    return discord.Embed(
        title='Error',
        description=f'Dis donc je ne suis pas dans ta tête il faut donner une ville!',
        color=error_color
    )
