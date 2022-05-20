import discord
import json
import requests
from keep_alive import keep_alive

# Import pour cacher le token
# Source : https://www.youtube.com/watch?v=SLd4d5EqbiM
import os
from dotenv import load_dotenv

# Import des fonction liées à l'analyse de sentiment sur le ficher "sentiment.py"
from sentiment import sentiment
from setChannel import setChannel, nomValide

# Import des fonctions liées à la meteo sur le ficher "fonction_meteo.py"
from meteo import *

# Import des fonction liées à la date sur le ficher "date.py"
from date import date

# Import des fonction liées à la date sur le ficher "event.py"
from event import event, load_event
# Import des fonction liées à help sur le ficher "help.py"
from help import *


# Import des fonctions liées à sondage sur le fichier "sondage.py"
from sondage import *

# Import des fonctions liées à blague sur le fichier "blague.py"
from blague import *

from search import *

# Le token doit être défini dans un fichier d'environnement "config"
load_dotenv(dotenv_path="config")

# on  rajoute les intents dans le code en créant une instance de la classe d>
default_intents = discord.Intents.default()
# activer les intents relatifs aux membres:par défaut, la valeur de members >
default_intents.members = True
client = discord.Client(intents=default_intents)

# Variable
api_key = "5518aaa356e63d150a56dd90a999424b"
command_prefix_meteo = "!meteo"
command_prefix_help = "!help"

# On récupère les noms des channels à partir du fichier "channel.json"
with open('channel.json', "r") as f:
    channels = json.load(f)


@client.event
async def on_ready():
    """
    None -> None
    Evenement qui se déclanche quand le bot est prêt
    """
    print("Le bot est prêt")
    # Ajoute un bandeau "Joue à !help"
    await client.change_presence(activity=discord.Game('!help'))
    # Reprend les évènement en cours
    await load_event(client)


@client.event
async def on_message(message):
    """
    Message -> None
    message : Message discord récupérer quand un message est envoyé
    Evenement qui se déclanche quand le bot détecte un message
    """
    # On récupère le nom des channels
    channelSentiment = channels['sentiment']

    channelGeneral = channels['general']

    channelAccueil = channels['accueil']

    # Si le message viens de lui même ne fais rien et sort
    if message.author == client.user:
        return

    # Vérifie si le channel du message est channelSentiment
    if message.channel.name == channelSentiment:
        # Si le message commence par !setSentiment alors on appelle la fonction pour changer le nom du channel
        if message.content.startswith('!setSentiment'):
            await message.channel.send(setChannel(message.content, "sentiment", channels))
            # Réagit avec un checkmark si le nom a bien été changer
            if nomValide(message.content.split()[1:]):
                await message.add_reaction("✅")
        # Sinon on envoie un message avec le sentiment du message
        else:
            # Si le message commence par ! (est une commande) ne fais rien
            if not(message.content.startswith('!')):
                await message.channel.send(sentiment(message.content))

    # vérifie si le channel du message est channelGeneral
    if message.channel.name == channelGeneral:
        # Si le message commence par !setGeneral alors on appelle la fonction pour changer le nom du channel
        if message.content.startswith('!setGeneral'):
            await message.channel.send(setChannel(message.content, "general", channels))
            # Réagit avec un checkmark si le nom a bien été changer
            if nomValide(message.content.split()[1:]):
                await message.add_reaction("✅")

        # Appel la fonction date si le message est "!date"
        # fonctionnalité date
        if message.content.lower() == "!date":
            await message.channel.send(date())

        # fonctionnalité sondage
        if message.content.startswith("!sondage"):
            await sondage(message, message.content.split(";")[1], message.content.split(";")[2:])

        # fonctionnalité search
        if message.content.lower().startswith("!search"):
            await message.channel.send(rechercher(message.content))

        # fonctionnalité blague
        if message.content == "!blague":
            await message.channel.send(blagueExec())

        # vérifie si le channel du message est le bon
        if message.content.startswith("!event"):
            await event(message)

        # Appel la fonction meteo si le message commence par "!meteo"
        if message.content.startswith(command_prefix_meteo):
            # Remplace !meteo par rien pour avoir que la localisation et qu'il y est au moins 1 lettre après !meteo (exemple : !meteo p)
            if len(message.content.replace(command_prefix_meteo, '')) >= 1:
                # Stocke le contenu du message sans le !meteo et le converti en minuscule
                localisation = message.content.replace(
                    command_prefix_meteo, '').lower()
                # url contient l'url du site sur la localisation et dont l'unité est le Celsus
                url = f'http://api.openweathermap.org/data/2.5/weather?q={localisation}&appid={api_key}&units=metric'
                try:
                    data = parse_data(json.loads(
                        requests.get(url).content)['main'])  # Demande de prendre le contenu de l'url et de la convertir en json  #main = catégorie où se trouve les données qui nous interresse
                    # Appel de la fonction weather_message stocké dans embed #Le bot envoie dans le channel tout le contenu

                    await message.channel.send(embed=weather_message(data, localisation))
                except KeyError:
                    # Appel de la fonction error_message stocké dans embed
                    await message.channel.send(embed=error_message(localisation))

        # Si le message envoyé n'est pas le bot et que le contenu commence par !help
        if message.content.startswith(command_prefix_help):
            await message.channel.send(embed=help_message1())
            await message.channel.send(embed=help_message2())
            await message.channel.send(embed=help_message3())

    # vérifie si le channel du message est channelAccueil
    if message.channel.name == channelAccueil:
        # Si le message commence par !setAccueil alors on appelle la fonction pour changer le nom du channel
        if message.content.startswith('!setAccueil'):
            await message.channel.send(setChannel(message.content, "accueil", channels))
            # Réagit avec un checkmark si le nom a bien été changer
            if nomValide(message.content.split()[1:]):
                await message.add_reaction("✅")


@client.event
async def on_member_join(member):
    """
    Member -> None
    member : Membre discord récupérer quand un membre rejoint une guilde
    Evenement qui se déclanche quand le bot détecte rejoint une guilde
    """
    channelAccueil = channels['accueil']
    # Cherche le salon accuei pour envoyer le message d'accueil
    for i in range(len(member.guild.channels)):
        if member.guild.channels[i].name == channelAccueil:
            await member.guild.channels[i].send(content=f"Hola {member.display_name} !")
            # N'envoie pas le message sur plusieurs salon accueil du même nom
            return

    # https://www.docstring.fr/blog/creer-un-bot-discord-avec-python/

keep_alive()
# Lance le bot correpsondant au TOKEN
client.run(os.getenv("TOKEN"))
