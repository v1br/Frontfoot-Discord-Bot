# Environment Variables
from dotenv import load_dotenv
import os

load_dotenv()

# Standard library imports
import discord
import os

# Local application imports
from scripts import chat
from scripts import exceptions
from scripts import responses
from scripts import server

# global variables
intents = discord.Intents().all()
client = discord.Client(intents=intents)
devmode = False

# on_ready event
@client.event
async def on_ready():
  print(f'{client.user} is now online!')
  chat.begin(devmode)

# on_message event
@client.event
async def on_message(message):
  author = message.author
  channel = message.channel
  command = "NULL"

  # ignore self
  if author == client.user:
    return

  # read input
  command = chat.parse(message)
  if command == "NULL":
    return
  else:
    print(f"\nUser: {author}, Channel: {channel}\n-> {command}")

  # check status
  if devmode and command in ["status"]: #override
    pass
  
  elif devmode and isinstance(channel, discord.DMChannel):
    reply = exceptions.PROMPT["maintenance"]
    await message.channel.send(reply)
    return

  elif devmode and channel.name != "workshop":
    reply = exceptions.PROMPT["maintenance"]
    await message.channel.send(reply)
    return

  # show cards
  
  if command in ["help", "changelog", "menu", "roll", "roll d2", "roll d4", "roll d6", "roll d8", "roll d10", "roll d12", "roll d20", "roll d100", "send", "status"]:
    embed = chat.fetch(command)
    await message.channel.send(embed = embed)
    print(f"\nBot: ff, Channel: {channel.name}\n-> Card:{embed.title}")

  # show actions
  elif command in ["dance", "horn", "fishpole", "hotsauce", "shuriken"]:
    await message.channel.send(file = chat.perform(command))
    print(f"\nBot: ff, Channel: {channel.name}\n-> Gif:{command}")

  # show messages
  else: 
    reply = chat.run(command, author)
    await message.channel.send(reply)
    print(f"\nBot: ff, Channel: {channel.name}\n-> {reply}")


# driver function
def activate_bot():
  server.keep_alive()
  client.run(os.environ['TOKEN'])

