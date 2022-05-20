#on veut tester la fonctionnalité Search
#on importe le module qu'on veut tester 
#on importe la notion de tests unitaires avec python

import unittest
from bot import on_message
from search import rechercher

#la classe TestSearch hérite des éléments de la classe unittest.TestCase
class TestSearch(unittest.TestCase):
    def testOn_message(self):
        expected = rechercher("!search hello")
        r = on_message("!search hello")
        self.assertEqual(r,expected)

if __name__ == "__main__":
    unittest.main()

#https://www.youtube.com/watch?v=D8wdAYwH-ng&t=33s