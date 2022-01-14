import asyncio
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)

# help pages
page1 = discord.Embed(title="Daily Rewards", description="Players can now receive rewards each day they login!"
                                                         "\nUse the command /daily to open the rewards menu!"
                                                         "\nDon't like commands?"
                                                         "\nUse the Daily Rewards chest at the **Survival Spawn**!",
                      colour=discord.Colour.purple())
page1.set_image(url = 'https://i.ibb.co/C5rXQXr/8b3049e02fb3abde6e7e89715187cc0d342118bb721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af.png')
page2 = discord.Embed(title="Player Levels", description="Players have the ability to level up their player levels in two types of ways on **OAFACraft**."
                                                         "\nPlayers have **XP Level** as well as **Server Level**."
                                                         "\n**XP Level** uses the default XP levels of Minecraft to dictate mob leveling, difficulty, modifiers and more."
                                                         "\n\n**Server Level** is shown as a number next to the player's name in chat and is acquired by performing all actions including chat!",
                      colour=discord.Colour.purple())
page2.set_image(url = 'https://i.ibb.co/kczBN2r/Server-Level.png')
page3 = discord.Embed(title="Increased Health", description="You may notice your health raised to a base of **40 Hearts!**"
                                                            "\nThis occurs after recieving your first **Daily Reward!**"
                                                            "\nThis is to help ensure with the higher level difficulty of mobs and the leveling system that you will still be able to survive!",
                      colour=discord.Colour.purple())
page3.set_image(url = 'https://i.ibb.co/vQCsbPJ/40bars.png')
page4 = discord.Embed(title="Player Stats", description="Players now have upgradeable stats!"
                                                        "\nUse the command **/stats** to check in game!"
                                                        "\nUpgrading these stats as you play benefits the player!"
                                                        "\n\n**Strength:**"
                                                        "\nIncreases attack damage."
                                                        "\n*-Upgraded through Foraging, Fighting, Sorcery, Farming and Archery.*"
                                                        "\n\n**Health:**"
                                                        "\nIncreases the amount of HP you have."
                                                        "\n*-Upgraded through Fishing, Alchemy, Healing, Defense and Farming.*"
                                                        "\n\n**Regeneration:**"
                                                        "\nRecovers how fast you recover health."
                                                        "\n*-Upgraded through Fighting, Endurance, Healing, Excavation, and Agility.*"
                                                        "\n\n**Luck:** \nIncreases chance of getting rare loot from mobs, fishing, and more."
                                                        "\n*-Upgraded through Enchanting, Fishing, Mining, Excavation, and Archery.*"
                                                        "\n\n**Wisdom:**\nIncreases experience gained and decreases anvil costs."
                                                        "\n*-Upgraded through Enchanting, Alchemy, Sorcery, Forging, and Agility.*"
                                                        "\n\n**Toughness:**"
                                                        "\nIncreases the amount of damage reduced from enemy attacks."
                                                        "\n*-Upgraded through Foraging, Mining, Endurance, Defense, and Forging.*",
                      colour=discord.Colour.purple())
page4.set_image(url = 'https://i.ibb.co/mS84Gv1/Stats.png')
page5 = discord.Embed(title="Player Skills", description="Players can level up their skills to level up their stats as well as unlock useful passive abilities!"
                                                         "\nUse the command **/skills** to check in game!"
                                                         "\nThere are a total of **15** skills which reward **2** stats each!"
                                                         "\n**Farming**"
                                                         "\n*- Harvest crops to earn Farming XP*"
                                                         "\n**Foraging**"
                                                         "\n*- Cut trees to earn Foraging XP*"
                                                         "\n**Mining**"
                                                         "\n*- Mine stone and ores to earn Mining XP*"
                                                         "\n**Fishing**"
                                                         "\n*- Catch fish to earn Fishing XP*"
                                                         "\n**Excavation**"
                                                         "\n*- Dig with a shovel to earn Excavation XP*"
                                                         "\n**Archery**"
                                                         "\n*- Shoot mobs and players with a bow to earn Archery XP*"
                                                         "\n**Defense**"
                                                         "\n*- Take damage from entities to earn Defense XP*"
                                                         "\n**Fighting**"
                                                         "\n*- Fight mobs with melee weapons to earn Fighting XP*"
                                                         "\n**Endurance**"
                                                         "\n*- Walk and run to earn Endurance XP*"
                                                         "\n**Agility**"
                                                         "\n*- Jump and take fall damage to earn Agility XP*"
                                                         "\n**Alchemy**"
                                                         "\n*- Brew potions to earn Alchemy XP*"
                                                         "\n**Enchanting**"
                                                         "\n*- Enchant items and books to earn Enchanting XP*"
                                                         "\n**Sorcery**"
                                                         "\n*- Use mana abilities to earn Sorcery XP*"
                                                         "\n**Healing**"
                                                         "\n*- Drink and splash potions to earn Healing XP*"
                                                         "\n**Forging**"
                                                         "\n*- Combine and apply books in an anvil to earn Forging XP*",
                      colour=discord.Colour.purple())
page5.set_image(url = 'https://i.ibb.co/9n1wHyV/Skills.png')
page6 = discord.Embed(title="Player Movements", description="\nPlayers now have the ability to sit, stand, spin, and crawl!"
                                                            "\nYou can even sit on stairs as as a chair!"
                                                            "\nStand on the chair and put in the **/sit** command!"
                                                            "\nFit in 1x1 spaces by using the **/crawl** command!"
                                                            "\nTake a load off and use the **/lay** command!"
                                                            "\nOr go crazy and spin it out with **/spin**!",
                      colour=discord.Colour.purple())
page6.set_image(url = 'https://i.ibb.co/ZzMkL0L/Sit.png')
page7 = discord.Embed(title="Player Horses", description="Players now start with their own upgradeable mount!"
                                                         "\n\nCommands:"
                                                         "\n**/horse** - Opens player *Stables*, left clicking horse summons horse, right clicking opens *Options* menu"
                                                         "\n\n**/horse claim** - Claim a wild horse, must be riding",
                      colour=discord.Colour.purple())
page7.set_image(url = 'https://i.ibb.co/S33YPpH/Horses.png')
page8 = discord.Embed(title="Player Trading", description="Players can now secure trade!"
                                                          "\nInstead of tossing items on the ground, and running the risk of being ninja'd on "
                                                          "\nsome loot!"
                                                          "\n\nSimply type in the following commands:"
                                                          "\n**/trade [player name]** - Sends trade request"
                                                          "\n**/trade accept** - Accepts trade"
                                                          "\n**/trade deny** - Denies trade",
                      colour=discord.Colour.purple())
page8.set_image(url = 'https://i.ibb.co/C5rXQXr/8b3049e02fb3abde6e7e89715187cc0d342118bb721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af.png')
page9 = discord.Embed(title="Player Graves", description="Now when a player dies, a *protected* grave is spawned that holds the player's dropped items!"
                                                         "\nThe player also recieves a compass that shows them the way back!",
                      colour=discord.Colour.purple())
page9.set_image(url = 'https://i.ibb.co/P6pp5cF/Graves.png')
page10 = discord.Embed(title="Playtime", description="Players can now view their play time!"
                                                     "\n**/playtime** - Shows players play time",
                      colour=discord.Colour.purple())
page10.set_image(url = 'https://i.ibb.co/7gcR0Sw/Play-Times.png')
page11 = discord.Embed(title="Experience Bottles", description="Players can now bottle their XP using glass bottles and an enchanting table!"
                                                               "\n\nMust be XP level 10 or higher to bottle!"
                                                               "\n\nThen use the bottle to replenish your levels when needed!",
                      colour=discord.Colour.purple())
page11.set_image(url = 'https://i.ibb.co/PZDJHdV/XPBottling.png')
page12 = discord.Embed(title="Quests", description="Players can learn rewards by completing **Quests**!"
                                                   "\nSimply type in **/quest** and select one of the available quests!"
                                                   "\nRewards provided upon completion!",
                      colour=discord.Colour.purple())
page12.set_image(url = 'https://i.ibb.co/4s19xNq/Quests.png')
page13 = discord.Embed(title="Codex", description="Players can also track down collectibles, locations, and even hunting logs for mobs all in the **Codex**!"
                                                  "\nSimply type in **/codex** to start hunting!",
                      colour=discord.Colour.purple())
page13.set_image(url = 'https://i.ibb.co/qRV62ft/Codex.png')
page14 = discord.Embed(title="One Player Sleep", description="When you have multiple players on a server at the same time, it can be difficult to organize everyone to hop into bed to skip the night!"
                                                             "\n\nThis plugin fixes that by allowing only player needed to be in bed to skip the night!",
                      colour=discord.Colour.purple())
page14.set_image(url = 'https://i.ibb.co/cwYWcMD/Sleep-Most.png')
page15 = discord.Embed(title="Bed Regenerate", description="Players now regenerate their health while sleeping!",
                      colour=discord.Colour.purple())
page15.set_image(url = 'https://i.ibb.co/C5rXQXr/8b3049e02fb3abde6e7e89715187cc0d342118bb721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af.png')
page16 = discord.Embed(title="MORE COMING SOON", description="CHECK BACK FOR UPDATES",
                      colour=discord.Colour.purple())
page16.set_image(url = 'https://i.ibb.co/Hp0TJCF/721f8a3035fc4095bd7041a671d465c23e8e6f3acd4792cab903cc6ee0af2eed68fdd4d76f3b8a00da39a3ee5e6b4b0d3255.png')

bot.help_pages = [page1, page2, page3, page4, page5, page6, page7, page8, page9, page10, page11, page12, page13, page14, page15, page16]


@bot.event
async def on_ready():
    print(bot.user.name + " is ready.")


@bot.command()
async def player(ctx):
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