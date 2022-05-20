# https://gist.github.com/billyeatcookies/7a6fd3dfa1da7f25d621920aa36babb4

import discord
import asyncio


async def sondage(ctx, message, choix):
    """
    object X Str X List -> Embed / String
    ctx : objet qui permet de déclancher des actions
    message : message de l'évènement 
    choix : liste des choix de l'évènement
    Fonction permettant de générer un sondage sous forme d'embed puis annonce des résultats
    """
    # on vérifie qu'il y a au moins 2 choix et maximum 10 choix
    if len(choix) <= 1:
        await ctx.channel.send("Vous devez mettre au minimum 2 choix et au maximum 10 choix.")
        return

    if len(choix) > 10:
        await ctx.channel.send("Vous devez mettre au minimum 2 choix et au maximum 10 choix.")
        return
    else:
        reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣',
                     '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
        # on va énumerer les choix proposés et les associés chacune à une emoji qu'on mettra dans une liste
        description = []
        for x, option in enumerate(choix):
            description += '\n {} {}'.format(reactions[x], option)
        # on affiche le sondage et cette liste sous forme d'embed
        embed = discord.Embed(title=message, description=''.join(description))
        sdge = await ctx.channel.send(embed=embed)
        # on ajoute les réactions sur l'embed
        for reaction in reactions[:len(choix)]:
            await sdge.add_reaction(reaction)

        # on interrompt le code pendant 90secondes
        await asyncio.sleep(90)
        # on récupere l'id de l'embed
        msg = await ctx.channel.fetch_message(sdge.id)
        gagnant_reaction = []
        gagnant_reaction_nombre = 0

        # on parcourt les réactions dans l'embed
        for reaction in msg.reactions:
            # si le nombre de votes sur la réaction est le plus élévé
            if (reaction.count - 1) > gagnant_reaction_nombre:
                # on récupère le gagnant des votes
                gagnant_reaction.append(reaction.emoji)
                # on récupère le nombre de votes
                gagnant_reaction_nombre = reaction.count - 1
            # s'il y a des égalités
            elif (reaction.count - 1) == gagnant_reaction_nombre != 0:
                # on récupère les gagnants
                gagnant_reaction.append(reaction.emoji)

        # s'il n'y pas de votes
        if gagnant_reaction_nombre == 0:
            await ctx.channel.send("Les votes sont finis, personne n'a voté.")

        # s'il y a 1 gagnant
        if len(gagnant_reaction) == 1:
            # on transforme la liste en String
            gagnant_reaction = " ".join(gagnant_reaction)
            # on affiche le résultat
            await ctx.channel.send(f"Les votes sont finis, la réaction n°{(gagnant_reaction)} a eu le plus de vote avec {gagnant_reaction_nombre} votes. ")

        # s'il y a plusieurs gagnants
        elif len(gagnant_reaction) > 1:
            # on transforme la liste en String
            gagnant_reaction = " ".join(gagnant_reaction)
            # on affiche le résultat
            await ctx.channel.send(f"Les votes sont finis, nous avons eu une égalité, les réaction n°{gagnant_reaction} ont eu le plus de vote avec {gagnant_reaction_nombre} votes.")
