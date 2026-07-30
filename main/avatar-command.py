import discord
from discord.ext import commands
from discord import app_commands
import webbrowser
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

    @discord.ui.button(label="Open Browser",style=discord.ButtonStyle.secondary)
    async def call(self,interaction:discord.Interaction,button:discord.ui.Button):
        webbrowser.open(self.link)
        await interaction.response.send_message("Done!",ephemeral=True)
        await interaction.delete_original_response()

@bot.command()
async def av(ctx:commands.Context):
    embed=discord.Embed(color=colorRandom())
    image=ctx.author.display_avatar.url
    embed.set_image(url=image)
    button=AButton(image)
    await ctx.send(embed=embed,view=button)

bot.run("TOKEN")
#solved interaction problem! just make sure that interaction comes in the three seconds, don't let defer win!
#it will work, a button will come and by clicking on it, a new website will open which will be your pfp but it will still show that an error happened, of time out, which makes sense because you are not using an interaction
#a view or layout view needs interaction, even app commands, slash commands need and if you are not using it, then it wouldn't have defear which gives time to the interaction, and if there's no defer then interaction only has three seconds
#and there's a lot about it
