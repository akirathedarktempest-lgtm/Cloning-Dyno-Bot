import discord
from discord.ext import commands
from discord import app_commands
import sqlite3
import time
import csv
import asyncio

intents=discord.Intents.all()
bot=commands.Bot(command_prefix=commands.when_mentioned_or("?"),intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready to work!")
    await bot.tree.sync()

def checkNames(guild:int,user:int):
    connect=sqlite3.connect(f"{guild} Server.db")
    cursor=connect.cursor()
    cursor.execute("SELECT * FROM afkSet")
    info=cursor.fetchall()
    for i in info:
        if i[0]==user:
            return True
        else:
            pass
    return False

def checkGuild(guild:int):
    with open("guilds.csv","r") as file:
        info=csv.reader(file)
        for i in info:
            data=i[0]
            if type(data) is str:
                data=int(data)
            if guild==data:
                return True
            else:
                pass
        return False

def listNames(guild:int):
    connect=sqlite3.connect(f"{guild} Server.db")
    cursor=connect.cursor()
    cursor.execute("SELECT * FROM afkSet")
    l=[]
    info=cursor.fetchall()
    connect.close()
    for i in info:
        l.append([i[0],i[1],i[2]])
    return l

@bot.tree.command()
async def set_afk(interaction:discord.Interaction,message:str):
    await interaction.response.defer()
    connect=sqlite3.connect(f"{interaction.guild.id} Server.db")
    cursor=connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS afkSet(
                        user INTEGER,
                        name TEXT,
                        intialTime INTEGER,
                        status TEXT)""")
    cursor.execute(f"INSERT INTO afkSet VALUES (?,?,?,?)",[interaction.user.id,interaction.user.global_name,int(time.time()),"AFK"])
    connect.commit()
    connect.close()
    await interaction.followup.send(f"{interaction.user.mention}! I have set you AFK: {message}")
    if checkGuild(interaction.guild.id) is False:
        with open("guilds.csv","a",newline='') as file:
            info=csv.writer(file)
            info.writerow([interaction.guild.id])
    else:
        pass

@bot.event
async def on_message(message:discord.Message):
    if message.author==bot.user:
        return
    if checkGuild(message.guild.id) is False:
        pass
    else:
        if checkNames(message.guild.id,message.author.id) is True:
            channel=message.guild.get_channel(message.channel.id)
            msg=await channel.send(f"Welcome back {message.author.mention}!!!")
            await asyncio.sleep(8)
            await msg.delete()
            connect=sqlite3.connect(f"{message.guild.id} Server.db")
            cursor=connect.cursor()
            cursor.execute(f"DELETE FROM afkSet WHERE user={message.author.id}")
            connect.commit()
            connect.close()
            await bot.process_commands(message)
            return
        else:
            for i in listNames(message.guild.id):
                if f"<@{i[0]}>" in message.content:
                    channel=message.guild.get_channel(message.channel.id)
                    await channel.send(f"{i[1]} is on AFK from {int(time.time())-i[2]} seconds!")
                    break
                else:
                    pass
    await bot.process_commands(message)

bot.run("TOKEN")
#HAHA...this...this thing almost killed me...haha
