import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="Supply Drops", description="Players now have a chance for a random supply drop to fall near them!"
                                                        "\nPlayers can find from food to diamonds in these chests!"
                                                        "\nEven **OAFA TOKENS**!",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://i.ibb.co/C5rXQXr/8b3049e02fb3abde6e7e89715187cc0d342118bb721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af.png')
page2 = discord.Embed(title="Item Sorter", description="Forget redstone with the **ItemSorter**"
                                                       "\nNo more lag!"
                                                       "\n\nCreate your own **Item Sorter** by following the below steps:"
                                                       "\n**1.** Place down the chest you want to designate for input of items!"
                                                       "\n**2.** Type in command: `/ics add sender`!"
                                                       "\n**3.** With the newly acquired *Wooden Hoe*, right click the **Input Chest** you placed in *Step 1*!"
                                                       "\n**4.** Place down the chests you would like items sorted into!"
                                                       "\n**5.** Type in command `/ics add receiver`!"
                                                       "\n**6.** With the newly acquired *Wooden Hoe*, right the **Storage Chests** you placed in *Step 4* to designate as storage!"
                                                       "\n**7.** Place an item frame on each of your storage chests!"
                                                       "\n**8.** In the item frames, place the items you want each chest to hold!"
                                                       "\n**9.** Leave an item frame blank to have it catch the items not sorted!"
                                                       "\n**10.** Profit!",
                      colour=discord.Colour.purple())
page2.set_image(url = 'https://i.ibb.co/T46CRKZ/2020-03-11-19-56-00.png')
page3 = discord.Embed(title="Custom Collectibles", description="Players can now hunt for custom collectibles including statues, items, and even plushies!"
                                                               "\n\nMobs have a small chance at dropping a collectible, or you might even find something interesting fishing!"
                                                               "\n\nCollect em' all!",
                      colour=discord.Colour.purple())
page3.set_image(url = 'https://i.ibb.co/SyjqwZs/Collectibles.png')
page4 = discord.Embed(title="Custom Arrows", description="Mobs now have a small chance to drop different types of custom arrows!"
                                                         "\nPlayers can also craft these using **DropCrafting**!",
                      colour=discord.Colour.purple())
page4.set_image(url = 'https://i.ibb.co/KbdKTKc/Custom-Arrows.png')
page5 = discord.Embed(title="Custom Blocks", description="**Note:** Bedrock players experience large amounts of lag when able to view custom head blocks."
                                                         "\nCustom head blocks have been disabled for Bedrock players until a better solution is available."
                                                         "\nPlayers can now use custom heads as objects in game, or use them as a mask!"
                                                         "\n\n**Commands:** "
                                                         "\n**/skulls** - Opens a custom objects GUI, allows for favorites",
                      colour=discord.Colour.purple())
page5.set_image(url = 'https://i.ibb.co/DW4nMs3/Custom-Blocks.png')
page6 = discord.Embed(title="Custom Consumables", description="Custom consumable items drop from mobs on occasion!"
                                                              "\nConsumables can be crafted using the **DropCrafting** system!",
                      colour=discord.Colour.purple())
page6.set_image(url = 'https://i.ibb.co/S6ypJ0S/Consumables.png')
page7 = discord.Embed(title="Wandering Collector", description="Some items never get picked up."
                                                               "\nThey end up despawning, and in some cases, you wish you could have a second a chance at obtaining some of these items!"
                                                               "\nMeet the **Wandering Collector**!"
                                                               "\nWandering Traders now collect despawned items and put them for trade!",
                      colour=discord.Colour.purple())
page7.set_image(url = 'https://i.ibb.co/x1qpwp4/Wandering-Collector.png')
page8 = discord.Embed(title="Arrow Pickup", description="Players can now pick up arrows shot by mobs automatically!"
                                                        "\nNo more annoying stacks of skeleton arrows everywhere!",
                      colour=discord.Colour.purple())
page8.set_image(url = 'https://i.ibb.co/Pcjy5nF/Arrow-Pickup.png')
page9 = discord.Embed(title="MORE COMING SOON", description="CHECK BACK FOR UPDATES",
                      colour=discord.Colour.purple())
page9.set_image(url = 'https://i.ibb.co/Hp0TJCF/721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af2eed68fdd4d76f3b8a00da39a3ee5e6b4b0d3255.png')

bot.help_pages = [page1, page2, page3, page4, page5, page6, page7, page8, page9]


@bot.event
async def on_ready():
    print(bot.user.name + " is ready.")


@bot.command()
async def item(ctx):
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