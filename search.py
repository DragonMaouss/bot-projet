# googlesearch et search permettent d'extraire des informations d'un site web
from googlesearch import search

message = ""


def rechercher(message):
    """
    String -> string
    message : contenue du Message disord (le !search)
    fonction permettant de générer deux liens de recherche en rapport avec le sujet
    """
    retour = ""
    # on ne garde que ce qui suit "!search" dans la variable recherche
    recherche = message.lower()[7:]
    retour += "Voici ce que vous cherchez :" + "\n"
    # tld: signifie domaine de premier niveau, ce qui signifie que nous voulons rechercher notre résultat sur google.com ou google.in ou un autre domaine
    # num: nombre de résultats que nous voulons
    # stop: dernier résultat à récupèrer. Il faudrait utiliser None pour continuer à  chercher indÃ©finiment
    for j in search(recherche, tld="co.in", num=3, stop=2):
        retour += j + "\n"

    return retour

# https://fr.acervolima.com/effectuer-une-recherche-google-a-laide-du-code-python/
