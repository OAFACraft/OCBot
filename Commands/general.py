import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="Falling Stars", description="Players now have a chance to see shooting stars at night!"
                                            "\nOccasionally one of these stars will fall to the ground!"
                                            "\nLocate these fallen stars for rewards!"
                                            "\n\nDuring a **New Moon** you might see a meteor shower with an increased amount of **Falling Stars**! ",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://i.ibb.co/4RZSVYw/Falling-Stars.png')
page2 = discord.Embed(title="Fishing 2.0", description="Custom fish! New fish! More fish!"
                                                       "\nSee fish size! Different rarity fish!"
                                                       "\nFish fish fish!"
                                                       "\n\nNote: Bedrock users may see graphical issues with custom heads."
                                                       "\nMost notably, it will be a Steve head.",
                      colour=discord.Colour.purple())
page2.set_image(url = 'https://i.ibb.co/W5MLFdQ/Fishing.png')
page3 = discord.Embed(title="Dynmap", description="See the world in a different way!"
                                                  "\nFind things in game from your web browser!"
                                                  "\n\n**http://173.237.28.184:8123/**",
                      colour=discord.Colour.purple())
page3.set_image(url = 'https://i.ibb.co/0VxQDVS/map.png')
page4 = discord.Embed(title="Custom NPC's", description="Players can find and interact with tons of custom NPC's throughout the world!"
                                                        "\nFrom informational to interactive, there's always new NPC's being added!",
                      colour=discord.Colour.purple())
page4.set_image(url = 'https://i.ibb.co/WF0bNmm/2022-01-14-14-22-35.png')
page5 = discord.Embed(title="Custom Ores", description="Players can now find custom ores as they mine!"
                                                       "From experience, to even kelp to eat while underground, there are loads to discover!",
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
async def general(ctx):
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