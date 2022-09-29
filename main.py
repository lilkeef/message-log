import nextcord
from nextcord import commands
import asyncio
import random
from nextcord.utils import get

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot Online")

@client.event 
async def on_message_delete(message):
    embed = nextcord.Embed(title=f"{message.author.name} has deleted the message | {message.author.id}", description=f"`{message.content}`")
    channel = client.get_channel()#channel id 
    await channel.send(embed=embed)

@client.event
async def on_message_edit(message_before, message_after):
    embed = nextcord.Embed(title=f"{message_before.author.name} has edited the message | {message_before.author.id}")
    embed.add_field(name="Before Message", value=f"{message_before.content}", inline=False)
    embed.add_field(name="After Message", value=f"{message_after.content}", inline=False)
    channel = client.get_channel()#channel id
    await channel.send(embed=embed)

@client.run("")#token bot
