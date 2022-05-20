import unittest
from email import message
from bot import on_message
from help import help_message


class Test_On_Message_Meteo(unittest.TestCase):
    def test_On_Message_Help(self):
        r = on_message(message)
        if (message.content.lower().startwith("!help")):
            self.assertEqual(r, help_message())


if __name__ == "__main__":
    unittest.main()
