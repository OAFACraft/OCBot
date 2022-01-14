import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="Land Claiming", description="Players have the ability to claim their own little section of property by using a **golden shovel**!"
                                                         "\nBy right clicking at one corner, and then clicking at the opposite corner of the space you'd like to claim, you'll see the blocks update to confirm the claim!"
                                                         "\nVertical space included!"
                                                         "\n\n**/abandonclaim** - Deletes the claim you are in"
                                                         "\n**/claimexplosions** - Toggles explosions allowed in the claim"
                                                         "\n**/trust** - Gives another player permission to edit in your claim"
                                                         "\n**/untrust** - Revokes any permissions granted to a player in your claim"
                                                         "\n**/accesstrust** - Gives a player permission to use your buttons, levers, and beds"
                                                         "\n**/containertrust** - Gives a player permission to use your buttons, levers, beds, crafting gear, containers, and animals."
                                                         "\n**/trustlist** - Lists the permissions for the claim you are standing in\n**/subdivideclaims** - Switches your shovel to subdivision mode"
                                                         "\n**/restrictsubclaim** - Restricts a subdivision to inherit no permissions from parent claim\n**/basicclaims** - Puts shovel back in basic claims mode"
                                                         "\n**/untrust all** - Removes all permission for all players in your claim"
                                                         "\n**/abandonallclaims** - Deletes all of your claims"
                                                         "\n**/givepet** - Gives away a tamed animal",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://i.ibb.co/f0tzDNP/Claims.png')
page2 = discord.Embed(title="Protected Chests", description="Players can now protect their chests from griefing!"
                                                            "\nProtect your chest!"
                                                            "\n\n**/pyc chestgui** - Opens the Chest GUI"
                                                            "\n**/pyc protect** - Protect targeted chest"
                                                            "\n**/pyc unprotect** - Remove protection of targeted chest you own"
                                                            "\n**/pyc info** - Shows owner and friends of target chest"
                                                            "\n**/pyc addFriend [name]** - Allow a friend(s) to access targeted chest"
                                                            "\n**/pyc removeFriend [name]** - Remove friend(s) access to targeted chest"
                                                            "\n**/pyc addFriendAll [name]** - Add a single friend to all of your chests"
                                                            "\n**/pyc removeFriendAll [name]** - Remove a single friend from your chests"
                                                            "\n**/pyc list [options]** - List with default options you can enable"
                                                            "\n**/pyc list addFriends [name] or [name,name,name]** - Add a single friend to all of your registered chests, no target required"
                                                            "\n**/pyc list removeFriends [name] or [name,name,name]** - Remove a single friend from all of your registered chests, no target required"
                                                            "\n**/pyc list reset** - Resets your list configuration"
                                                            "\n**/pyc list mylist** - Shows your list with your default settings",
                      colour=discord.Colour.purple())
page2.set_image(url = 'https://i.ibb.co/2kmnght/Protected-Chests.png')
page3 = discord.Embed(title="Protected Drops", description="Certain mobs now will drop their items in protected loot boxes!"
                                                           "\n\n**Affected Mobs**:"
                                                           "\nEnder Dragon"
                                                           "\nWither",
                      colour=discord.Colour.purple())
page3.set_image(url = 'https://i.ibb.co/yRvSGyv/Protected-Drops.png')
page4 = discord.Embed(title="Keycard / Keypad", description="Players can now craft Keycards and Keypads!"
                                                            "\nSpecific level keycards! Up to Level 5!"
                                                            "\nPersonalized keypads!",
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
async def security(ctx):
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