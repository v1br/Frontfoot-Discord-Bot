# Environment Variables
from dotenv import load_dotenv
import os
load_dotenv()

# Standard library imports
import datetime
import discord
import os

# Local application imports
from scripts import chat
from scripts import exceptions
from scripts import server

# global variables
intents = discord.Intents().all()
client = discord.Client(intents=intents)
developer = os.environ['DEVELOPER']
devmode = False

# on_ready event
@client.event
async def on_ready():
  print(f'{client.user} is now online!')
  chat.begin({
    'devmode' : devmode,
    'launch_time' : datetime.datetime.now(),
    'client' : client
  })

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
  keyword = command.split(" ")[0]

  if command == "NULL":
    return
  else:
    print(f"\nUser: {author}, Channel: {channel}\n-> {command}")

  # check status
  if devmode:
    if command in ["status", "changelog"] or author.name == developer: 
      pass
    else:
      reply = exceptions.PROMPT["maintenance"]
      await message.channel.send(reply)
      return

  # show cards
  if keyword in ["help", "changelog", "menu", "roll", "status", "8ball"]:
    embed = chat.fetch(command)
    await message.channel.send(embed = embed)
    print(f"\nBot: ff, Channel: {channel.name}\n-> Card:{embed.title}")

  # show messages
  else: 
    reply = chat.run(command, author)
    await message.channel.send(reply)
    print(f"\nBot: ff, Channel: {channel.name}\n-> {reply}")


# driver function
def activate_bot():
  server.keep_alive()
  client.run(os.environ['TOKEN'])

