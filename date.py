# datetime: librairie python fournissant des mÃ©thodes liÃ©es Ã  la manipulation des dates et des temps
import datetime


def date():
    """
    None -> string
    fonction permettant de donner la date du jour et le temps actuel
    """
    # retour:chaine de caractÃ¨res permettant de stocker le rÃ©sultat
    # strftime() : fonction permettant de  formater l'affichage de la date.Elle utilise en premier paramÃ¨tre le format de la date Ã  afficher et en deuxiÃ¨me paramÃ¨tre la date
    retour = "La date d'aujourd'hui est:\n" + \
        datetime.datetime.today().strftime('%Y-%m-%d')
    return retour


# https://www.journaldunet.fr/web-tech/developpement/1202881-comment-recuperer-l-heure-actuelle-en-python/#:~:text=Pour%20obtenir%20la%20date%20et,appeler%20la%20m%C3%A9thode%20time().&text=Pour%20obtenir%20une%20date%20plus,date%20en%20cha%C3%AEne%20de%20caract%C3%A8res.
