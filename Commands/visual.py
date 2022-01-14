import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="Health Display", description="Players will now be able to see the life remaining of entities on both the action bar, as well as the mob's name bar!",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://i.ibb.co/WHQjTbW/nycw-Ru-Lr8-Z.png')
page2 = discord.Embed(title="Damage Display", description="Players can now see damage and health as it happens!"
                                                          "\nDamage numbers baby!",
                      colour=discord.Colour.purple())
page2.set_image(url = 'https://i.ibb.co/fkqWTrh/2017-05-04-22-15-39.png')
page3 = discord.Embed(title="Interactions Visualized", description="Players can now watch interactions such as crafting, brewing, furnaces, and much more, happen in front of their eyes!"
                                                                   "\nWatch items emerge from chests!"
                                                                   "\nItems crafted on the table in front of you!",
                      colour=discord.Colour.purple())
page3.set_image(url = 'https://i.ibb.co/CK0fRsy/418bbe700e80b56c331fa769287a5ba2811a8121.gif')
page4 = discord.Embed(title="Nighttime Effects", description="Night time particle effects!"
                                                             "\n**Mystical**!",
                      colour=discord.Colour.purple())
page4.set_image(url = 'https://i.ibb.co/C5rXQXr/8b3049e02fb3abde6e7e89715187cc0d342118bb721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af.png')
page5 = discord.Embed(title="MORE COMING SOON", description="CHECK BACK FOR UPDATES",
                      colour=discord.Colour.purple())
page5.set_image(url = 'https://i.ibb.co/Hp0TJCF/721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af2eed68fdd4d76f3b8a00da39a3ee5e6b4b0d3255.png')

bot.help_pages = [page1, page2, page3, page4, page5]


@bot.event
async def on_ready():
    print(bot.user.name + " is ready.")


@bot.command()
async def visual(ctx):
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"]  # skip to start, left, right, skip to end
    current = 0
    msg = await ctx.send(embed=bot.help_pages[current], delete_after=120.0)

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