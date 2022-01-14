import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="ONCE AND FOR ALL", description="**O.A.F.A.** is an exclusive discord club that developes communities, stemming from individual growth."
                                                            "\nOur services include:"
                                                            "\nA classy discord server."
                                                            "\nPremium features and bots."
                                                            "\nActivity and events."
                                                            "\nPromotions and sponsorships."
                                                            "\nContracts to design and build servers."
                                                            "\nAppraise and review community standards."
                                                            "\nHuman resources and support."
                                                            "\nGame hosting on private servers."
                                                            "\nA staff training program."
                                                            "\nOpportunity for growth within the community ladder. "
                                                            "\nWe challenge ourselves to break the boundaries of self indulgence and build an empire for people, forming communities, compelled with a burning desire to make a difference in their world. "
                                                            "\nWithin the online domain, stemming from Discord, we provide people, *casual users and gamers*, with the opportunity to impact the experiences of others through their inclusion in activities and events, hosted by **O.A.F.A.** and other affiliated communities."
                                                            "\n\n`Rally the troops and lead the victory charge, holding the banner we all believe in.\nWe will be the change; we will make the difference, once and for all!`"
                                                            "\n - Quote by John Woodson, founder of **Once And For All**"
                                                            "\n\n**http://discord.gg/onceandforall**",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://i.ibb.co/Q81t9YK/Pixaloop-13-04-2021-23-07-42-9180000.gif')

bot.help_pages = [page1]


@bot.event
async def on_ready():
    print(bot.user.name + " is ready.")


@bot.command()
async def oafa(ctx):
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