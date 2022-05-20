# on veut tester la fonctionnalité sentiment
# on importe le module qu'on veut tester
# on importe la notion de tests unitaires avec python


import unittest
from sentiment import analyseSentiment

# la classe TestSearch hÃ©rite des Ã©lÃ©ments de la classe unittest.TestCase


class TestSentiment(unittest.TestCase):
    def testSentiment(self):
        r = analyseSentiment("très heureux")
        self.assertEqual(
            r, "Très positif")
        r = analyseSentiment("un peu content")
        self.assertEqual(
            r, "Positif")
        r = analyseSentiment("patate")
        self.assertEqual(
            r, "Neutre")
        r = analyseSentiment("triste")
        self.assertEqual(
            r, "Négatif")
        r = analyseSentiment("très triste")
        self.assertEqual(
            r, "Très négatif \nTu as l'air triste, je vais te raconter une blague")


if __name__ == "__main__":
    unittest.main()
