# on veut tester la fonctionnalité setChannel
# on importe le module qu'on veut tester
# on importe la notion de tests unitaires avec python


import unittest
from setChannel import setChannel

# la classe TestSearch hÃ©rite des Ã©lÃ©ments de la classe unittest.TestCase


class TestSetChannel(unittest.TestCase):

    def testSetChannel(self):
        channels = {"sentiment": "sentiment",
                    "general": "general", "accueil": "accueil"}

        r = setChannel("!setSentiment test1", "sentiment", channels)
        self.assertEqual(
            r, "Le nouveau nom du channel sentiment est "+channels["sentiment"])

        r = setChannel("!setSentiment test2", "general", channels)
        self.assertEqual(
            r, "Le nouveau nom du channel general est "+channels["general"])

        r = setChannel("!setSentiment test3", "accueil", channels)
        self.assertEqual(
            r, "Le nouveau nom du channel accueil est "+channels["accueil"])


if __name__ == "__main__":
    unittest.main()
