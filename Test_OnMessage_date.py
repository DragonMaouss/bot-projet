#on veut tester la fonctionnalité Date
#on importe le module qu'on veut tester 
#on importe la notion de tests unitaires avec python

import unittest
from bot import on_message
from date import date

#la classe TestDate hérite des éléments de la classe unittest.TestCase
class testOnmessage_date(unittest.TestCase):
    def testOn_message(self):

        expected = date("!date")
        r = on_message("!date")

        self.assertEqual(r,expected)

if __name__ == "__main__":
    unittest.main()

#https://www.youtube.com/watch?v=D8wdAYwH-ng&t=33s

