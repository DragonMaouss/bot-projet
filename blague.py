# https://www.delftstack.com/fr/howto/python/count-the-number-of-files-in-a-directory-in-python/

import random
import os


def file():
    """
    None -> Int
    Fonction qui retourne le nombre de fichiers dans le dossier "blagues"
    """
    # on récupère les fichiers blague dans le dossier "blagues"
    nombre_blague = 0
    dir = "blagues"
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            nombre_blague += 1
    return nombre_blague


def blagueExec():
    """
    None -> String
    Fonction qui execute la fonction blague
    """
    # on génère un numéro aléatoire parmi le nombre de fichiers
    nombre_blague = file()
    numero = str(random.randint(1, nombre_blague))
    # on execute la fonction blague avec le numero
    b = blague(numero)
    return b


def blague(num):
    """
    String -> String
    num : le numéro du fichier contenant la blague
    Fonction qui retourne une blague
    """
    # on lit le fichier contenant une blague
    blague = open("blagues/blague"+num+".txt", "r", encoding="utf-8")
    rep = blague.read()
    blague.close()
    return rep
