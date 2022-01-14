import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="📄 All Recipes Unlocked 📄", description="Due to the nature of some of our plugins, the recipes for all items have been unlocked from the start for all players!",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://i.ibb.co/kc6v6Lw/2022-01-14-14-15-26.png')
page2 = discord.Embed(title="🛠️ Portable Crafting 🛠️", description="Players now have the ability to craft anywhere!\nNo table required!\nType in the command **/craft** to open your portable crafting table!",
                      colour=discord.Colour.purple())
page2.set_image(url = 'https://i.ibb.co/kBjtVp9/Portable-Craft.png')
page3 = discord.Embed(title="⚒️DropCrafting ⚒️", description="OAFACraft features a custom crafting method known as **DropCrafting**!\nSimply throwing the correct items together on the ground will result in some unique items and old favorites!",
                      colour=discord.Colour.purple())
page3.set_image(url = 'https://i.ibb.co/vHKnJ3K/Drop-To-Craft.png')
page4 = discord.Embed(title="⚒️Smelting ⚒️", description="Place your armor and tools into a furnace and recieve back the ingots used to craft them!\nThe amount of ingots provided is based upon durability of the item!",
                      colour=discord.Colour.purple())
page4.set_image(url = 'https://i.ibb.co/k3Wmd4J/MeltDown.png')
page5 = discord.Embed(title="📚 Disenchanting 📚", description="Players can now craft a custom extractor!\nUse it to extract an enchantment from an item and receive an enchanted book from it!",
                      colour=discord.Colour.purple())
page5.set_image(url = 'https://i.ibb.co/X3tznHX/f978532b153a839df52f800251b51110bfcdb02c.gif')
page6 = discord.Embed(title="MORE COMING SOON", description="CHECK BACK FOR UPDATES",
                      colour=discord.Colour.purple())
page6.set_image(url = 'https://i.ibb.co/Hp0TJCF/721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af2eed68fdd4d76f3b8a00da39a3ee5e6b4b0d3255.png')

bot.help_pages = [page1, page2, page3, page4, page5, page6]


@bot.event
async def on_ready():
    print(bot.user.name + " is ready.")


@bot.command()
async def craft(ctx):
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