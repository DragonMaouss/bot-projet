# Import API TextBlob et TextBlob_fr
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
# Import fonction blague pour le cas très négatif
from blague import blagueExec


# Source : https://github.com/DoubleGremlin181/Sentiment-Bot


def sentiment(message):
    """
    Str -> Str
    message : contenue du Message discord 
    Fonction qui analyse le sentiment donné en argument et renvoie le sentiment
    """
    # On récupère le sentiment du message (entre -1 et 1)
    sent = TextBlob(message, pos_tagger=PatternTagger(),
                    analyzer=PatternAnalyzer()).sentiment[0]
    # Renvoie le sentiment en fonction de son score
    if sent >= 0.5:
        return 'Très positif'
    elif (sent >= 0.25):
        return 'Positif'
    elif (sent > -0.25) and (sent < 0.25):
        return 'Neutre'
    elif (sent > -0.40):
        return 'Négatif'
    else:
        return "Très négatif \nTu as l'air triste, je vais te raconter une blague\n"+blagueExec()
