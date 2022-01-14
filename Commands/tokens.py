import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="OAFA Tokens", description="**OAFA Tokens** have a small chance to drop from any hostile mob!"
                                                       "\n**OAFA Tokens** are able to be turned into the **Token Master** located at the **Ruins of Pandora, or exchanged for items at the **Welcome Center**!"
                                                       "\nThese tokens are turned in for a randomly generated piece of ***Fabled*** gear!"
                                                       "\nSee the ***Fabled Gear*** module for further details!"
                                                       "\n\n**OAFA Tokens** can also be used as *Totems of Undying*, provided you have it in your offhand!",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://i.ibb.co/Qr1nrSr/OAFAToken.png')
page2 = discord.Embed(title="Token Master", description="Players can exchange their **OAFA Tokens** into the **Token Master** for **Fabled Gear**!"
                                                        "\nThe **Token Master** is located at the **Ruins of Pandora**!"
                                                        "\nHappy hunting!",
                      colour=discord.Colour.purple())
page2.set_image(url = 'https://i.ibb.co/RbmbrZs/Token-Master.png')
page3 = discord.Embed(title="Token Exchange", description="Located at the **Welcome Center** at **Survival Spawn**, the **Token Exchanger** and **Diamond Exchange** "
                                                          "allow players to trade in their **OAFA TOKENS** and/or *diamonds* in for each other! ",
                      colour=discord.Colour.purple())
page3.set_image(url = 'https://i.ibb.co/C5rXQXr/8b3049e02fb3abde6e7e89715187cc0d342118bb721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af.png')
page4 = discord.Embed(title="Fabled Gear", description="Turning in your **OAFA Tokens** into the **Token Master** will allow you to obtain a piece of randomly generated gear!"
                                                       "\nFeaturing enchantments, damage stats, the new **Durability 2.0** system, and even **Gems**, **Runes**, and **Essences** to socket into the gear!"
                                                       "\nHunt and grind for **your** perfect set!",
                      colour=discord.Colour.purple())
page4.set_image(url = 'https://i.ibb.co/ZGnMkL1/Fabled-Gear.png')
page5 = discord.Embed(title="World Bosses", description="Players can now craft **Boss Spawn Eggs**!"
                                                        "\nBy crafting and placing the egg, it spawns a **World Boss**!"
                                                        "\nPlayers will have a set time limit to defeat the boss for rewards!"
                                                        "\nRewards for all players involved!"
                                                        "\nRecipe:"
                                                        "\n*Coming Soon*",
                      colour=discord.Colour.purple())
page5.set_image(url = 'https://i.ibb.co/C5rXQXr/8b3049e02fb3abde6e7e89715187cc0d342118bb721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af.png')
page6 = discord.Embed(title="MORE COMING SOON", description="CHECK BACK FOR UPDATES",
                      colour=discord.Colour.purple())
page6.set_image(url = 'https://i.ibb.co/Hp0TJCF/721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af2eed68fdd4d76f3b8a00da39a3ee5e6b4b0d3255.png')

bot.help_pages = [page1, page2, page3, page4, page5, page6]


@bot.event
async def on_ready():
    print(bot.user.name + " is ready.")


@bot.command()
async def tokens(ctx):
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"]  # skip to start, left, right, skip to end
    current = 0
    msg = await ctx.send(embed=bot.help_pages[current], delete_after=180.0)

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