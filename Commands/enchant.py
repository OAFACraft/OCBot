import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="✨ Enchants ✨", description="There are now 5 different types of enchantments:"
                                                        "\n**Curse**, **Normal**, **Special**, **Spell**, and **Artifact**."
                                                        "\n\n**Normal**, **Special**, and **Artifact** enchantments are available from *Enchanting Tables*, *Villagers*, and *Loot Chests*."
                                                        "\n**Curse** enchantments are only available from *Villagers* and *Loot Chests*, just like in vanilla."
                                                        "\n\nLevels are calculated based on their cost. This is designed to be as similar to vanilla as possible."
                                                        "\n\nLoot chests will generally contain higher level enchantments."
                                                        "\n\nThis is also designed to be like vanilla, where enchantments in, for example, an end city will have a relatively high level.",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://i.ibb.co/Gn8x12K/Enchants.png')
page2 = discord.Embed(title="💀 Curses 💀", description="Below you will find a list of **Curse** enchantments that can be found with *Villagers*, or *Loot Chests*.",
                      colour=discord.Colour.purple())
page2.set_image(url = 'https://i.ibb.co/JjbNBRK/Curses.png')
page3 = discord.Embed(title="Normal - Armor", description="Below you will find a list of **Normal** enchantments that can be found with *Enchanting Tables*, *Villagers*, and *Loot Chests*.",
                      colour=discord.Colour.purple())
page3.set_image(url = 'https://i.ibb.co/bvWkG60/Normal-Armor.png')
page4 = discord.Embed(title="Normal - Boots / Helmets / Elytra", description="Below you will find a list of **Normal** enchantments that can be found with *Enchanting Tables*, *Villagers*, and *Loot Chests*.",
                      colour=discord.Colour.purple())
page4.set_image(url = 'https://i.ibb.co/5cC6ht7/Normal-Boots-Helmet-Elytra.jpg')
page5 = discord.Embed(title="Normal - Sword Only", description="Below you will find a list of **Normal** enchantments that can be found with *Enchanting Tables*, *Villagers*, and *Loot Chests*.",
                      colour=discord.Colour.purple())
page5.set_image(url = 'https://i.ibb.co/HdsxsZR/Normal-Swords.png')
page6 = discord.Embed(title="Normal - Sword + Axe", description="Below you will find a list of **Normal** enchantments that can be found with *Enchanting Tables*, *Villagers*, and *Loot Chests*.",
                      colour=discord.Colour.purple())
page6.set_image(url = 'https://i.ibb.co/WW4QS2x/Normal-Swords-Axes.jpg')
page7 = discord.Embed(title="Normal - Axe / Shears / Shield", description="Below you will find a list of **Normal** enchantments that can be found with *Enchanting Tables*, *Villagers*, and *Loot Chests*.",
                      colour=discord.Colour.purple())
page7.set_image(url = 'https://i.ibb.co/gM8P33p/Normal-Axe-Plus-Shield.jpg')
page8 = discord.Embed(title="Normal - Trident", description="Below you will find a list of **Normal** enchantments that can be found with *Enchanting Tables*, *Villagers*, and *Loot Chests*.",
                      colour=discord.Colour.purple())
page8.set_image(url = 'https://i.ibb.co/6nJCQDL/Normal-Tridents.png')
page9 = discord.Embed(title="Normal - Bow Only", description="Below you will find a list of **Normal** enchantments that can be found with *Enchanting Tables*, *Villagers*, and *Loot Chests*.",
                      colour=discord.Colour.purple())
page9.set_image(url = 'https://i.ibb.co/ZMsJMgD/Normal-Bow-Specific.png')
page10 = discord.Embed(title="Normal - Bows / Crossbows", description="Below you will find a list of **Normal** enchantments that can be found with *Enchanting Tables*, *Villagers*, and *Loot Chests*.",
                      colour=discord.Colour.purple())
page10.set_image(url = 'https://i.ibb.co/tXR3thX/Normal-Bow-Plus-Cross.png')
page11 = discord.Embed(title="Normal - Tool / Fishing Rod / General", description="Below you will find a list of **Normal** enchantments that can be found with *Enchanting Tables*, *Villagers*, and *Loot Chests*.",
                      colour=discord.Colour.purple())
page11.set_image(url = 'https://i.ibb.co/tXR3thX/Normal-Bow-Plus-Cross.png')
page12 = discord.Embed(title="🔥 Special - Enchantments 🔥", description="Below you will find a list of **Special** enchantments that can be found via the *Enchanting Table*, *Villagers*, and *Loot Chests*.",
                      colour=discord.Colour.purple())
page12.set_image(url = 'https://i.ibb.co/M2GQDxz/Special.png')
page13 = discord.Embed(title="🔮 Spell - Enchantments 🔮", description="Below you will find a list of **Spell** enchantments that can be found via the *Enchanting Table*, *Villagers*, and *Loot Chests*.",
                      colour=discord.Colour.purple())
page13.set_image(url = 'https://i.ibb.co/jbJVJxS/Spells.png')
page14 = discord.Embed(title="✨ Artifact ✨", description="**Artifact** enchantments are purely cosmetic enchantments.\nAn item can only have **one artifact enchantment at a time** and create particles depending on the item they're applied on."
                                                         "\n\n**Elytra** - Create a trail behind each wing\n\n**Melee Weapons** -  Create a spiral of particles around the victim"
                                                         "\n\n**Bows / Crossbows / Tridents** - Create a particle trail behind the projectile"
                                                         "\n\n**Pickaxes** - Create particles when breaking certain blocks",
                      colour=discord.Colour.purple())
page14.set_image(url = 'https://i.ibb.co/hKwrVWq/Artifact1.png')

bot.help_pages = [page1, page2, page3, page4, page5, page6, page7, page8, page9, page10, page11, page12, page13, page14]


@bot.event
async def on_ready():
    print(bot.user.name + " is ready.")


@bot.command()
async def enchant(ctx):
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"]  # skip to start, left, right, skip to end
    current = 0
    msg = await ctx.send(embed=bot.help_pages[current], delete_after=300.0)

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