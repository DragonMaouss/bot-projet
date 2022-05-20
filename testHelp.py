import unittest
from help import *
import json


class TestMeteo(unittest.TestCase):
    def testHelp(self):

        emoji_clown = "\U0001F921"
        emoji_weather = "\U00002600"
        emoji_event = "\U0001F389"
        emoji_day = "\U0001F4C6"
        emoji_search = "\U0001F50D"

        with open('channel.json', "r") as f:
            channels = json.load(f)

        channelGeneral = channels["general"]

        message = discord.Embed(
            title='**Comment utiliser le Bot**',
            description='Voici les différentes commandes utiles que vous pouvez retrouver dans notre bot',
            colour=discord.Colour.light_grey()
        )

        message.set_thumbnail(
            url='https://cdn-0.emojis.wiki/emoji-pics/microsoft/robot-microsoft.png')

        message.add_field(name=f'Salon général ({channelGeneral} actuellement)',
                          value='Les commandes ci-dessous sont utilisables seulement dans le salon general', inline=False)

        message.add_field(name='!blague',
                          value=f'Raconte une blague{emoji_clown}', inline=False)

        message.add_field(
            name='!date', value=f'Indique la date{emoji_day}', inline=False)

        message.add_field(name='!meteo [ville]',
                          value=f'Affiche la météo{emoji_weather}', inline=False)

        message.add_field(name='!search [PHRASE]',
                          value=f'Fait une recherche Google{emoji_search}', inline=False)

        message.add_field(
            name='!sondage [TITRE_SONDAGE] [CHOIX1] [CHOIX2] etc', value='Emet un sondage à choix multiple', inline=False)

        message.add_field(name='!event [EVENEMENT] [DATE] [HEURE]',
                          value=f'Programme un évènement{emoji_event}', inline=False)

        message.add_field(
            name='!setGeneral [nom]', value='Change le nom du salon général par le nouveau', inline=False)

        r = help_message1()
        self.assertEqual(len(r), len(message))


if __name__ == "__main__":
    unittest.main()
