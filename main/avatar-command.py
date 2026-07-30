import discord
from discord.ext import commands
from discord import app_commands
import webbrowser

intents=discord.Intents.all()
bot=commands.Bot(command_prefix=commands.when_mentioned_or("?"),intents=intents)

class AButton(discord.ui.View):
    def __init__(self,link):
        self.link=link
        super().__init__()

    @discord.ui.button(label="Open Browser",style=discord.ButtonStyle.secondary)
    async def call(self,interaction:discord.Interaction,button:discord.ui.Button):
        webbrowser.open(self.link)

@bot.command()
async def av(ctx:commands.Context):
    embed=discord.Embed()
    image=ctx.author.display_avatar.url
    embed.set_image(url=image)
    button=AButton(image)
    await ctx.send(embed=embed,view=button)

bot.run("TOKEN")
#it will work, a button will come and by clicking on it, a new website will open which will be your pfp but it will still show that an error happened, of time out, which makes sense because you are not using an interaction
#a view or layout view needs interaction, even app commands, slash commands need and if you are not using it, then it wouldn't have defear which gives time to the interaction, and if there's no defer then interaction only has three seconds
#and there's a lot about it
