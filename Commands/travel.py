import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="Home and SetHome", description="Players have the ability to set up to **10** different homes!"
                                                            "\nThese are teleport locations you can access at any point!"
                                                            "\nUse the **/sethome [name]** command to set a home!"
                                                            "\nUse the **/homes** command to return to a home!",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://i.ibb.co/rcLYt7r/Homes.png')
page2 = discord.Embed(title="Teleport Request", description="At request by players, you now have the ability to request to teleport  to another player, or teleport another player to you!"
                                                            "\n\n**/tpa [name]** - Request to teleport to player"
                                                            "\n**/tpahere [name]** - Request player to teleport to you"
                                                            "\n**/tpaccept** - Accept teleport request"
                                                            "\n**/tpacancel [name]** - Cancels a specific request"
                                                            "\n**/tpacancel** - Cancel all outstanding teleport requests",
                      colour=discord.Colour.purple())
page2.set_image(url = 'https://i.ibb.co/b1FJJVR/TPRequest.png')
page3 = discord.Embed(title="Elevators", description="Players now can **DropCraft** and utilize **Elevators** in their builds!"
                                                     "\n\n***Recipes:***"
                                                     "\n**White Elevator -**"
                                                     "\n*4 White Concrete + 1 Ender Pearl*"
                                                     "\n**Gray Elevator -**"
                                                     "\n*4 White Concrete + 1 Ender Pearl*"
                                                     "\n**Black Elevator -**"
                                                     "\n*4 White Concrete + 1 Ender Pearl*",
                      colour=discord.Colour.purple())
page3.set_image(url = 'https://i.ibb.co/xmDvPLf/Elevators.png')
page4 = discord.Embed(title="MORE COMING SOON", description="CHECK BACK FOR UPDATES",
                      colour=discord.Colour.purple())
page4.set_image(url = 'https://i.ibb.co/Hp0TJCF/721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af2eed68fdd4d76f3b8a00da39a3ee5e6b4b0d3255.png')

bot.help_pages = [page1, page2, page3, page4]


@bot.event
async def on_ready():
    print(bot.user.name + " is ready.")


@bot.command()
async def travel(ctx):
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