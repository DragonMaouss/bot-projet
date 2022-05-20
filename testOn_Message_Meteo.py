
from email import message
import unittest
from bot import on_message
from meteo import weather_message


class Test_On_Message_Meteo(unittest.TestCase):
    def test_On_Message_Meteo(self):
        r = on_message(message)
        if (message.content.lower().startwith("!meteo")):
            self.assertEqual(r, weather_message(message))


if __name__ == "__main__":
    unittest.main()
