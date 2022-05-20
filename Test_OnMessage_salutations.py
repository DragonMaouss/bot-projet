#on veut tester la fonctionnalité Salutations
#on importe le module qu'on veut tester 

#on importe la notion de tests unitaires avec python
import unittest
from bot import on_member_join

#la classe TestSalutations hérite des éléments de la classe unittest.TestCase
class TestSalutations(unittest.TestCase):
    def testOn_member_join(self):

        r = on_member_join("rahms#6978")
        expected = "Hola rahms !"
        self.Equal(r,expected)

if __name__ == "__main__":
    unittest.main()

#https://www.youtube.com/watch?v=D8wdAYwH-ng&t=33s