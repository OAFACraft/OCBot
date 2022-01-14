import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="Chat Color", description="Players can now set their color for text in the chat!"
                                                      "\n\n**Commands:**"
                                                      "\n**/color gui** - Opens up color selection",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://i.ibb.co/Xy05LPv/gui.png')
page2 = discord.Embed(title="Marriage", description="Players can now get married!"
                                                    "\nThis provides a host of perks to both players!"
                                                    "\n\n**/marry tp** - Teleports to the partner"
                                                    "\n**/marry sethome** - Sets the home for two married players"
                                                    "\n**/marry home** - Teleports to the home of married players"
                                                    "\n**/marry chat** - Allows to chat a couple private"
                                                    "\n**/marry chat toggle** - Toggles the chat to send all chat messages to the partner instead of to the public"
                                                    "\n**/marry pvpon** - Turns PvP between two married players on"
                                                    "\n**/marry pvpoff** - Turns PvP between two married players off"
                                                    "\n**/marry kiss** - To kiss your partner"
                                                    "\n**/marry gift** - Gifts the item in your hand to your partner"
                                                    "\n**/marry backpack** - Opens the backpack of your partner"
                                                    "\n**/marry backpack on** - Allows your partner to use your backpack"
                                                    "\n**/marry backpack off** - Disallows your partner to use your backpack"
                                                    "\n**/marry me** - Sends a player a marry request",
                      colour=discord.Colour.purple())
page2.set_image(url = 'https://i.ibb.co/s2VmNCT/Marriage.png')
page3 = discord.Embed(title="Link To Items", description="Players can **Link To Items** in chat and provide a way for other players to see their items or even their inventories!"
                                                         "\n\n**Commands:**"
                                                         "\n**[i]** - Will be replaced with link to item in hand"
                                                         "\n**/showinv** - Will display a link to your whole inventory",
                      colour=discord.Colour.purple())
page3.set_image(url = 'https://i.ibb.co/7QvtvCg/Item-Display.png')
page4 = discord.Embed(title="Piggy Back", description="Players can now pick up other players, animals, villagers, and more!"
                                                      "\nThis can help with moving entities around or just for fun!"
                                                      "\nStack up to 2 entities on your head!"
                                                      "\nCraft a saddle and while holding in your hand, right click an entity!"
                                                      "\nCrouch to let go!",
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
async def social(ctx):
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