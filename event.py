from asyncio import sleep
import datetime
import json


async def event(message):
    """
    Message -> None
    message : Message discord qui envoie la commande !event
    Fonction principale 
    """
    # On récupère le temps saisie
    eventTime = getEventTime(message.content)
    if eventTime == False:
        await message.channel.send(
            "Oubli pas de me donner l'évènement, la date et l'heure\nExemple : !event 'Prochain palindrome' 21/12/2112 21:12")
    await send_event(datetime.datetime.now(), eventTime, message)


def getEventTime(content):
    """
    Str -> datetime / Boolean
    content : contenue du Message discord (le !event) 
    Fonction qui renvoie le temps saisie 
    """
    # On récupère le contenue du message sans le "!event"
    content = content.split()[1:]

    # Si le contenue n'a pas de temps on demande de respecter le format
    if len(content) <= 1:
        return False

    # Si le contenue a 3 de longueur
    elif len(content) >= 3:
        # On vérifie que le temps saisie est dans le bon format
        try:
            # On récupère la date et l'heure
            eventTime = datetime.datetime.strptime(
                content[-2]+content[-1], '%d/%m/%Y%H:%M')
        # On demande de respecter le format si il y a une erreur
        except ValueError:
            return False

    # Si le contenue a 2 de longueur
    elif len(content) >= 2:
        # On vérifie que le temps saisie est dans le bon format
        try:
            # On récupère la date et l'heure sera  à minuit
            eventTime = datetime.datetime.strptime(
                content[-1], '%d/%m/%Y')
        # On demande de respecter le format si il y a une erreur
        except ValueError:
            return False
    # Renvoie le temps saisie
    return eventTime


def getMessage(content):
    """
    Str -> Str
    content : contenue du Message discord (le !event) 
    Fonction qui récupère et renvoie le message donnée
    """
    # Initialisation
    message = ""
    finMessage = 0

    # Parcour le message entier et renvoie l'indice de la fin du message
    for i in range(len(content.split())):
        if content.split()[i].endswith('"') or content.split()[i].endswith("'"):
            finMessage = i-1

    # Recréer le message entier sans les "" ou '' au
    for i in range(finMessage+1):
        message += content.split()[i+1].strip('"').strip("'")+" "

    return message


async def send_event(now, eventTime,  event,  events={}):
    """
    Datetime X Datetime X Message X Dict -> None
    now : date et heure actuel (au moment du !event ou au moment du load_event )
    eventTime : date et heure de l'évènement récupéré avec getEventTime
    event : Message discord qui envoie la commande !event
    events : dictionnaires qui contient les évènement en cours et fini avec les informations nécessaires pour les continuer
    Fonction qui envoie le message et le rappel
    """
    # Calcul le temps restant en seconde
    wait_time = (eventTime-now).total_seconds()

    # Si le "events" n'a pas été mis en argument c'est à dire si il ne s'agit pas d'évènement chargé
    if events == {}:
        # Si le temps est déjà passé
        if eventTime < now:
            # Envoie un message qui indique que le temps est déjà passé
            await event.reply("Sauf si tu as une machine a remonté dans le temps c'est trop tard")
            return
        # Si le temps n'est pas encore passé
        else:
            # On récupère les évènement de "events.json"
            with open('events.json', "r") as f:
                events = json.load(f)

            # Envoie un message qui décrit l'évènement et le récupère
            eventMessage = await event.channel.send("Évènement : "+getMessage(event.content)+"\nLe " + toFrench(eventTime))

            # Ajoute l'id du message, le temps demandé, l'utilisateur et le channel dans les 'runningEvents' de events
            events['runningEvents'][str(event.id)] = (
                str(eventTime), str(event.channel.id))

            # Ecrit les changment dans le fichier json
            with open('events.json', "w") as f:
                json.dump(events, f)

            # Attend jusqu'au temps demandé
            await sleep(wait_time)

            # Envoie un message pour le rappel
            await eventMessage.reply("C'est maintenant "+event.author.mention + " !")

            # Supprime l'évènement qui vient de finir
            del events['runningEvents'][str(event.id)]

            # Met à jour le fichier json
            with open('events.json', "w") as f:
                json.dump(events, f)

    # Si il s'agit d'évènement chargé
    else:
        # Attend jusqu'au temps demandé
        await sleep(wait_time)
        # Envoie un message pour le rappel
        await event.reply("C'est maintenant "+event.author.mention + " !")


async def load_event(client):
    """
    Client -> None
    client : Client discord correspondant au bot
    Fonction qui reprend les évènement déjà lancé
    """
    # On récupère les évènement de "events.json"
    with open('events.json', "r") as f:
        events = json.load(f)

    # Parcour les évènement en cours
    for keys, values in events["runningEvents"].items():
        # Récupère le message originel
        eventChannel = await client.fetch_channel(int(values[1]))
        event = await eventChannel.fetch_message(int(keys))
        # Si le temps n'est pas déjà passé
        if datetime.datetime.now() < datetime.datetime.fromisoformat(values[0]):
            # Reprend la fonction send_event pour le rappel
            await send_event(datetime.datetime.now(), datetime.datetime.fromisoformat(values[0]), event, events)
        # Ajoute l'évènement dans les "finishedEvents"
        events['finishedEvents'][keys] = (values[0])
        # Met à jour le fichier json
        with open('events.json', "w") as f:
            json.dump(events, f)

    # Parcour les évènement finie
    for finishedEvent in events["finishedEvents"]:
        # Supprime les évènements en cours qui sont dans les évènements finie
        del events["runningEvents"][finishedEvent]
    # Efface les évènements finie
    events['finishedEvents'] = {}
    # Met à jour le fichier json
    with open('events.json', "w") as f:
        json.dump(events, f)


def toFrench(eventTime):
    """
    Datetime -> String
    eventTime : date et heure de l'évènement récupéré avec getEventTime
    Fonction qui tranforme le temps en une phrase en français
    """
    # Récupère le jour et le mois en anglais
    jour = eventTime.strftime("%a")
    mois = eventTime.strftime("%b")

    # Change le jour en français
    if (jour == "Mon"):
        jour = "lundi"
    elif (jour == "Tue"):
        jour = "mardi"
    elif (jour == "Wed"):
        jour = "mercredi"
    elif (jour == "Thu"):
        jour = "jeudi"
    elif (jour == "Fri"):
        jour = "vendredi"
    elif (jour == "Sat"):
        jour = "samedi"
    elif (jour == "Sun"):
        jour = "dimanche"

    # Change le mois en français
    if mois == "Jan":
        mois = "janvier"
    elif (mois == "Feb"):
        mois = "février"
    elif (mois == "Mar"):
        mois = "mars"
    elif (mois == "Apr"):
        mois = "avril"
    elif (mois == "May"):
        mois = "mai"
    elif (mois == "Jun"):
        mois = "juin"
    elif (mois == "Jul"):
        mois = "juillet"
    elif (mois == "Aug"):
        mois = "août"
    elif (mois == "Sep"):
        mois = "septembre"
    elif (mois == "Oct"):
        mois = "octobre"
    elif (mois == "Nov"):
        mois = "novembre"
    elif (mois == "Dec"):
        mois = "décembre"

    # Renvoie une chaine de charactère qui décrit la date en français
    return jour+" "+eventTime.strftime("%d")+" "+mois+" "+eventTime.strftime("%Y")+" à "+eventTime.strftime("%X")[0:5]
