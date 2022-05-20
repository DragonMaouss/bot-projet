#on veut tester la fonctionnalité Date
#on importe le module qu'on veut tester
#on importe la notion de tests unitaires avec python
import unittest
from blague import *

class TestBlague(unittest.TestCase):
    def testBlague(self):
        b = blague("1")
        self.assertEqual(b,"Comment appelle-t-on un alligator qui enquête?\nUn investi-gator.\n")

        b1 = blague("11")
        self.assertEqual(b1,"Qu'est-ce qu'un cochon volant ?\nUn aéroport.")

        b2 = blague("27")
        self.assertEqual(b2,"J'ai une blague sur les magasins\nMais elle a pas supermarché")

if __name__=="__main__":
    unittest.main()

