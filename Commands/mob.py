import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="Leveled Mobs", description="Mobs spawn now in leveled tiers!"
                                                        "\nThe level of the mobs around you is directly tied to your XP level as well as your distance from spawn!"
                                                        "\nThe higher your level, the higher the mobs!"
                                                        "\nThe further you are, the stronger the mobs!",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://i.ibb.co/xSPNyxJ/Mob-Levels.png')
page2 = discord.Embed(title="Mob Heads", description="All mobs now have a chance to drop their head!"
                                                     "\nHeads show player name of who killed mob!"
                                                     "\nCollect them all!",
                      colour=discord.Colour.purple())
page2.set_image(url = 'https://i.ibb.co/X2hzJSV/MobHeads.png')
page3 = discord.Embed(title="Confetti Creepers", description="Creepers are the bane of Minecraft existence."
                                                             "\nNow they are as colorful as a grunt birthday party!"
                                                             "\nNow with *reduced damage*! Enjoy!",
                      colour=discord.Colour.purple())
page3.set_image(url = 'https://i.ibb.co/C5rXQXr/8b3049e02fb3abde6e7e89715187cc0d342118bb721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af.png')
page4 = discord.Embed(title="Giant Phantoms", description="Players may notice something a little off about Phantoms lately..."
                                                          "\nStay up for more than a few nights, and you might find yourself squaring off against **GIANT** Phantoms!"
                                                          "\nPhantom size will scale based on how many nights you stay up!"
                                                          "\n\nWell at least you'll see them coming...",
                      colour=discord.Colour.purple())
page4.set_image(url = 'https://i.ibb.co/C5rXQXr/8b3049e02fb3abde6e7e89715187cc0d342118bb721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af.png')
page5 = discord.Embed(title="Dragon Stats", description="When taking on the Ender Dragon, players should now see certain stats!"
                                                        "\nPlayers should see statistics showing damage leaderboards and more!",
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
async def mob(ctx):
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