import discord
from discord.ext import commands

SecretT = "PUT HERE YOUR TOKEN"

#change prefix here
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
	print(f'{client.user} is now ON!')



client.run(SecretT)	