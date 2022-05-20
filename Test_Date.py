#on veut tester la fonctionnalité Date
#on importe le module qu'on veut tester 
#on importe la notion de tests unitaires avec python
import unittest
from date import date
#la classe TestDate hérite des éléments de la classe unittest.TestCase
class TestDate(unittest.TestCase):
    def testDate(self):
        r = date("!date")
        self.assertEqual(r,"La date d'aujourd'hui est:\n2022-04-14")
if __name__ == "__main__":
    unittest.main()

#https://www.youtube.com/watch?v=D8wdAYwH-ng&t=33s