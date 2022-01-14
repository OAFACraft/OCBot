import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="Durability 2.0", description="***Fabled*** gear features the new **Durability 2.0** system!"
                                                          "\nUse **NPC's** titled **Blacksmith** to repair these items, or **Crouch / Sneak** click any anvil! ",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://i.ibb.co/sJh3zqf/Dura2.png')
page2 = discord.Embed(title="Gems, Runes, and Essences", description="Fabled gear features the ability to socket Gems, Runes, and Essences!"
                                                                     "\nGems, Runes, and Essences can be socketed into a Fabled piece of gear to enhance and increase your stats even more!"
                                                                     "\nTo socket any Gems, Runes, and Essences you can either choose to visit any Rune Enscriber, Gem Socketer, or Essence Mage NPC's to have a better success rate, or you can choose to drag and drop the Gem, Rune, or Essence onto the item to have a smaller chance of success!"
                                                                     "\nGems, Runes, and Essences have a small chance to drop from any hostile mobs!",
                      colour=discord.Colour.purple())
page2.set_image(url = 'https://i.ibb.co/2tHYGRR/2022-01-14-14-20-06.png')
page3 = discord.Embed(title="Extraction", description="Players can remove Gems, Runes, and Essences via two methods!"
                                                      "\nFirstly, they can visit any Extractor NPC to remove with a slightly higher chance of success."
                                                      "\nSecondly, hostile mobs have a chance to drop Extraction Spells that can be used to remove socketed Gems, Runes, and Essences!"
                                                      "\n\n**Note**: You are **destroying** the currently socketed Gem, Rune, or Essence in the process!",
                      colour=discord.Colour.purple())
page3.set_image(url = 'https://i.ibb.co/0DvR6sD/Extraction.png')
page4 = discord.Embed(title="Dismantling", description="Players can get rid of their excess Gems, Runes, and Essences by dismantling them into materials!"
                                                       "\nSimply visit any Dismantler NPC!",
                      colour=discord.Colour.purple())
page4.set_image(url = 'https://i.ibb.co/sjXH3Wq/Dismantle.png')
page5 = discord.Embed(title="MORE COMING SOON", description="CHECK BACK FOR UPDATES",
                      colour=discord.Colour.purple())
page5.set_image(url = 'https://i.ibb.co/Hp0TJCF/721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af2eed68fdd4d76f3b8a00da39a3ee5e6b4b0d3255.png')

bot.help_pages = [page1, page2, page3, page4, page5]


@bot.event
async def on_ready():
    print(bot.user.name + " is ready.")


@bot.command()
async def fabled(ctx):
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