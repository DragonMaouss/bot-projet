# on veut tester la fonctionnalité event
# on importe le module qu'on veut tester
# on importe la notion de tests unitaires avec python


import unittest
import datetime
from event import getEventTime, toFrench

# la classe TestSearch hÃ©rite des Ã©lÃ©ments de la classe unittest.TestCase


class TestEvent(unittest.TestCase):
    def testEvent(self):
        r = getEventTime("!event test 21/12/2112 21:12")
        self.assertEqual(r, datetime.datetime(2112, 12, 21, 21, 12))
        r = toFrench(r)
        self.assertEqual(
            r, "mercredi 21 décembre 2112 à 21:12")


if __name__ == "__main__":
    unittest.main()
