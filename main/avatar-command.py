import discord
from discord.ext import commands
from discord import app_commands
import random

def colorRandom():
    hexColor=""
    for _ in range(6):
        hexColor+=random.choice("0123456789abcdef")
    return int(hexColor,16)

intents=discord.Intents.all()
bot=commands.Bot(command_prefix=commands.when_mentioned_or("?"),intents=intents)

class AButton(discord.ui.View):
    def __init__(self,link):
        self.link=link
        super().__init__()
        self.add_item(discord.ui.Button(url=self.link,style=discord.ButtonStyle.gray,label="Open Browser!"))

@bot.command()
async def av(ctx:commands.Context):
    embed=discord.Embed(color=colorRandom())
    image=ctx.author.display_avatar.url
    embed.set_image(url=image)
    button=AButton(image)
    await ctx.send(embed=embed,view=button)

bot.run("TOKEN")
