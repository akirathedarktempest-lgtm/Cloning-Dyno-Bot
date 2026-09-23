#i invited dyno to my bot, yeah!!!!!
#and first then the next thing i make

import discord
from discord.ext import commands
from discord import app_commands

intents=discord.Intents.all()
bot=commands.Bot("?",intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is ready!")

@bot.tree.command()
@app_commands.checks.has_permissions(manage_roles=True)
async def add_role(interaction:discord.Interaction,name:str,color:str):
    await interaction.response.defer(ephemeral=True)
    color=color.lower()
    for i in color:
        if i not in "0123456789abcdef":
            return await interaction.followup.send("Wrong color :(\n-# The letters must be in 0123456789abcdef")
    await interaction.guild.create_role(name=name,color=int(color,16))
    await interaction.followup.send("Done!",ephemeral=True)

bot.run("TOKEN")

#my server, you can may join https://discord.gg/aakyNnYNdM
#and then my testing server (in my first server, people just can't use slash commands, so you can talk there, here you can look at the tests) https://discord.gg/6nv6Ysaexx
