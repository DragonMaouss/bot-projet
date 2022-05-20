import unittest

from meteo import *


class TestMeteo(unittest.TestCase):
    def testMeteo(self):

        data = {"temp": 18.74, "feels_like": 18.39,
                "temp_min": 17.86, "temp_max": 20.85}
        localisation = "paris"

        localisation = localisation.title()
        message = discord.Embed(
            title=f'Meteo de {localisation}',
            color=color
        )
        message.set_thumbnail(
            url='https://image.winudf.com/v2/image1/b3JnLmFuZHJvd29ya3Mua2xhcmFfaWNvbl8xNjExMzc2NDc2XzAzMQ/icon.png?w=&fakeurl=1')
        for key in data:
            message.add_field(
                name=key_features[key],
                value=f'{str(data[key])}°C',
                inline=False
            )

        r = weather_message(data, localisation)
        self.assertEqual(len(r), len(message))

    def testParse_data(self):
        data = {"temp": 18.74, "feels_like": 18.39,
                "temp_min": 17.86, "temp_max": 20.85, "pressure": 1022, "humidity": 66}
        r = parse_data(data)
        self.assertEqual(r, {"temp": 18.74, "feels_like": 18.39,
                             "temp_min": 17.86, "temp_max": 20.85})


if __name__ == "__main__":
    unittest.main()
