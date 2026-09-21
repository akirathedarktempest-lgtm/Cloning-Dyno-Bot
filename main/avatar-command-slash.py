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

@bot.event
async def on_ready():
    print(f"{bot.user} is ready to work!")
    await bot.tree.sync()

class AButton(discord.ui.View):
    def __init__(self,link):
        self.link=link
        super().__init__()

    @discord.ui.button(label="Open Browser",style=discord.ButtonStyle.secondary)
    async def call(self,interaction:discord.Interaction,button:discord.ui.Button):
        webbrowser.open(self.link)
        await interaction.response.send_message("Done!",ephemeral=True)
        await interaction.delete_original_response()

@bot.tree.command()
@app_commands.allowed_contexts(guilds=True,dms=True,private_channels=True)
async def av(interaction:discord.Interaction,member:discord.Member|discord.User|None=None):#why discord.Member|discord.User?
    if interaction.guild is not None:#this command can also work in dms here now
        if member is None:#so, in dm it's not a Member, it's a User
            await interaction.response.defer()#so yeah, if you are in dms, User will run and in guild it will be Member
            embed=discord.Embed(color=colorRandom())
            image=interaction.user.display_avatar.url
            embed.set_image(url=image)
            button=AButton(image)
            await interaction.followup.send(embed=embed,view=button)
        elif member is not None:
            await interaction.response.defer()
            embed=discord.Embed(color=colorRandom(),description=f"{member.mention}")
            image=member.display_avatar.url
            embed.set_image(url=image)
            button=AButton(image)
            await interaction.followup.send(embed=embed,view=button)
        else:
            print("Something's wrong there :(")
    elif interaction.guild is None:
        if member is None:
            await interaction.response.defer()
            embed=discord.Embed(color=colorRandom())
            image=interaction.user.display_avatar.url
            embed.set_image(url=image)
            button=AButton(image)
            await interaction.followup.send(embed=embed,view=button)
        elif member is not None:
            await interaction.response.defer()
            embed=discord.Embed(color=colorRandom(),description=f"{member.mention}")
            image=member.display_avatar.url
            embed.set_image(url=image)
            button=AButton(image)
            await interaction.followup.send(embed=embed,view=button)
        else:
            print("Something's wrong!")
    else:
        return print("Wrong!")

bot.run("TOKEN")
#and all set!
