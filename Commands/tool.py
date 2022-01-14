import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="Leveled Tools", description="Tools now have levels and upgrades!"
                                            "\nJust by using the tools as you play, you will find them getting better and more efficient!"
                                                         "\nYou may also start to find enchantments appearing on them!",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://i.ibb.co/Qm1fv0t/Tool-Levels1.png')
page2 = discord.Embed(title="MORE COMING SOON", description="CHECK BACK FOR UPDATES",
                      colour=discord.Colour.purple())
page2.set_image(url = 'https://i.ibb.co/Hp0TJCF/721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af2eed68fdd4d76f3b8a00da39a3ee5e6b4b0d3255.png')

bot.help_pages = [page1, page2]


@bot.event
async def on_ready():
    print(bot.user.name + " is ready.")


@bot.command()
async def tool(ctx):
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