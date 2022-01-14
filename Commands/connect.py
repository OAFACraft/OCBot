import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="🌐 How To Connect 🌐", description="**FOR JAVA USERS:**\n**Server Name:** OAFACraft\n**Server Address:** onceandforall.apexmc.co\n**Ports:**\n**Java:** 25565\n**Bedrock:** 19132\n\n**FOR CONSOLE USERS**\nDownload the mobile application below for your device.\n**Android:** *MC Server Connector*\nhttps://play.google.com/store/apps/details?id=com.smokiem.mcserverconnector&hl=en_US&gl=US\n**Apple:** *BedrockTogether*\nhttps://apps.apple.com/us/app/bedrocktogether/id1534593376\n\nOnce installed, you will want to start the server connector on the mobile application, and add the below server information:\n**Server Address:** onceandforall.apexmc.co\n**Ports:**\n**Bedrock:** 19132\n\nLet the app continue running, and fully watch any advertisements that play to their completion. Once server is up and running on mobile application, you will see the server listed under your **Friends** list on Xbox, Playstation, or Switch.",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://probot.media/mn8aKsm8Hc.png')


bot.help_pages = [page1]


@bot.event
async def on_ready():
    print(bot.user.name + " is ready.")


@bot.command()
async def connect(ctx):
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"]  # skip to start, left, right, skip to end
    current = 0
    msg = await ctx.send(embed=bot.help_pages[current], delete_after=60.0)

    for button in buttons:
        await msg.add_reaction(button)

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", check=lambda reaction,
                                                                             user: user == ctx.author and reaction.emoji in buttons,
                                             )

        except asyncio.TimeoutError:
            return print("test")

        else:
            previous_page = current
            if reaction.emoji == u"\u23EA":
                current = 0

            elif reaction.emoji == u"\u2B05":
                if current > 0:
                    current -= 1

            elif reaction.emoji == u"\u27A1":
                if current < len(bot.help_pages) - 1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(bot.help_pages) - 1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=bot.help_pages[current])

#Run bot
bot.run("OTMwOTg5MzU0MTc4OTczNzE4.Yd95Zg.1KhvEQ8Gr4QnhgYQhopFoUWZaRw")