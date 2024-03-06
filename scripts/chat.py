# Standard library imports
import random
import discord
import datetime
import io
from discord.ext import commands
from PIL import Image, ImageSequence

# Local application imports
from scripts import exceptions
from scripts import responses

# Global variables
launch_time = "???"
sleeping = "???"

# Init bot variables
def begin(devmode):
  global sleeping
  global launch_time

  sleeping = devmode
  launch_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  print("Launched on--> " + launch_time) 

# Parse all statements
def parse(message):
  content = message.content.lower()
  content = content.strip()

  punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

  for x in content:
    if x in punc:
      content = content.replace(x, "")

  words = content.split(" ")
  if content.startswith("ff") or content.startswith("hey ff"):

    # handle edge-cases
    if (" " not in content and content != "ff"):
      return "NULL"

    # remove 'hey'
    if words[0] == "hey":
      words.pop(0)

    # remove 'ff'
    if words[0] == "ff":
      words.pop(0)

    # remove 'please'
    for w in words:
      if w == "please" or w == "pls" or w == "plz":
        words.remove(w)

    # reconstruct command
    return " ".join(words).strip()

  else:
    return "NULL"


# Perform actions if needed
def perform(command):
  
  gif_file = discord.File('./media/fishpole.gif', filename='penguin.gif')
  
  # dance
  if command == "dance":
    gif_path = './media/dance.gif'

  # fishpole
  elif command == "fishpole":
    gif_path = './media/fishpole.gif'

  # horn
  elif command == "horn":
    gif_path = './media/horn.gif'
  
  # hotsauce
  elif command == "hotsauce":
    gif_path = './media/hotsauce.gif'

  # shuriken
  elif command == "shuriken":
    gif_path = './media/shuriken.gif'
  
  gif_file = discord.File(gif_path, filename='penguin.gif')
  return gif_file


# Fetch cards if needed
def fetch(command):

  embed = discord.Embed(
    title = 'NULL',
    description = 'NULL',
    color = discord.Color.green()
  )
  
  # help
  if command == "help":
    card = responses.HELP()
    embed = discord.Embed(
        title = 'User Manual',
        description = card['desc'],
        color = discord.Color.green()
      )
  
    embed.add_field(name = 'Important stuff', value = card['note'], inline = False)
    embed.add_field(name = 'List of commands', value = card['list'], inline = False)
    embed.add_field(name = 'Developer\'s note', value = card['foot'], inline = False)
  
  # changelog
  elif command == "changelog":
    card = responses.CHANGELOG()
    embed = discord.Embed(
      title = 'Changelog',
      description = card['desc'],
      color = discord.Color.green()
    )
  
    embed.add_field(name = 'Updated on:', value = card['date'], inline = False)
    embed.add_field(name = 'Added:', value = card['add'], inline = False)
    embed.add_field(name = 'Fixed:', value = card['fix'], inline = False)

  # menu
  elif command == "menu":
    card = responses.MENU()
    embed = discord.Embed(
      title = 'Frontfoot\'s Kitchen Menu',
      description = card['desc'],
      color = discord.Color.orange()
    )

    embed.add_field(name = 'List of available dishes (command: ff cook)', value = card['food'], inline = False)
    embed.add_field(name = 'List of available drinks (command: ff serve)', value = card['drink'], inline = False)

  # status
  elif command == "status":
    card = responses.STATUS()
    embed = discord.Embed(
      title = 'Status Report',
      description = card['desc'],
      color = discord.Color.green()
    )

    embed.add_field(name = 'Developer Mode: ', value = sleeping, inline = False)
    embed.add_field(name = 'Last launched on: ', value = launch_time, inline = False)

  # roll
  elif command.startswith("roll"):
    score = 0
    action = "Nothing happened..."
    card = responses.ROLL()

    if command == "roll":
      embed = discord.Embed(
        title = 'Available dice rolls',
        description = card['desc'],
        color = discord.Color.purple(),
      )

      embed.add_field(name = 'Roll commands', value = card['list'], inline = True)
    

    else:
      if command == "roll d2":
        score = random.randint(1,2)
        action = "A coin was flipped to reveal a number."
  
      elif command == "roll d4":
        score = random.randint(1,4)
        action = "A tetrahedron was rolled to reveal a number."

      elif command == "roll d6":
        score = random.randint(1,6)
        action = "A regular six-sided die was rolled to reveal a number."

      elif command == "roll d8":
        score = random.randint(1,8)
        action = "An octahedron was rolled to reveal a number."

      elif command == "roll d10":
        score = random.randint(1,10)
        action = "An decahedron was rolled to reveal a number."

      elif command == "roll d12":
        score = random.randint(1,12)
        action = "An dodecahedron was rolled to reveal a number."

      elif command == "roll d20":
        score = random.randint(1,20)
        action = "An icosahedron was rolled to reveal a number."

      elif command == "roll d100":
        score = random.randint(1,100)
        action = "Two decahedrons were rolled to reveal a number."

  
      embed = discord.Embed(
        title = 'Dice Roll',
        description = action,
        color = discord.Color.purple()
      )
  
      embed.add_field(name = 'Result', value = score, inline = True)

  return embed

# Execute commands if needed
def run(command, user):
  reply = ""

  # blank
  if command == "":
    reply = random.choice(responses.WAIT())

  # bye
  elif command == "bye" or command == "goodbye":
    reply = random.choice(responses.GOODBYE())

  # cook
  elif command.startswith("cook"):

    if command == "cook":
      reply = "Sure, what do you want me to cook?"

    elif command == "cook bacon":
      reply = random.choice(responses.ORDER("bacon"))
      reply += " :bacon:"

    elif command == "cook bread":
      reply = random.choice(responses.ORDER("bread"))
      reply += " :french_bread:"

    elif command == "cook burger":
      reply = random.choice(responses.ORDER("burger"))
      reply += " :hamburger:"

    elif command == "cook cupcake":
      reply = random.choice(responses.ORDER("cupcake"))
      reply += " :cupcake:"

    elif command == "cook cheese":
      reply = random.choice(responses.ORDER("cheese"))
      reply += " :cheese:"

    elif command == "cook chicken":
      reply = random.choice(responses.ORDER("chicken"))
      reply += " :poultry_leg:"

    elif command == "cook croissant":
      reply = random.choice(responses.ORDER("croissant"))
      reply += " :croissant:"

    elif command == "cook custard":
      reply = random.choice(responses.ORDER('custard'))
      reply += " :custard:"

    elif command == "cook egg":
      reply = random.choice(responses.ORDER('egg'))
      reply += " :cooking:"

    elif command == "cook fish":
      reply = random.choice(responses.ORDER("fish"))
      reply += " :fish:"

    elif command == "cook flatbread":
      reply = random.choice(responses.ORDER("stuffed flatbread"))
      reply += " :stuffed_flatbread:"

    elif command == "cook fries":
      reply = random.choice(responses.ORDER("fries"))
      reply += " :fries:"

    elif command == "cook hotdog":
      reply = random.choice(responses.ORDER("hotdog"))
      reply += " :hotdog:"

    elif command == "cook mooncake":
      reply = random.choice(responses.ORDER("mooncake"))
      reply += " :moon_cake:"

    elif command == "cook pancake":
      reply = random.choice(responses.ORDER("pancake"))
      reply += " :pancakes:"

    elif command == "cook pie":
      reply = random.choice(responses.ORDER("pie"))
      reply += " :pie:"

    elif command == "cook pizza":
      reply = random.choice(responses.ORDER("pizza"))
      reply += " :pizza:"

    elif command == "cook salad":
      reply = random.choice(responses.ORDER("salad"))
      reply += " :salad:"

    elif command == "cook shrimp":
      reply = random.choice(responses.ORDER("shrimp"))
      reply += " :fried_shrimp:"

    elif command == "cook stew":
      reply = random.choice(responses.ORDER("stew"))
      reply += " :stew:"

    else:
      return exceptions.PROMPT["missing_recipe"]

  # explode
  elif command == "explode":
    reply += random.choice(responses.EXPLODE(user))
  
  # hello
  elif command == "hi" or command == "hello":
    reply = random.choice(responses.GREET())

  # insult
  elif command.startswith("insult"):

    if command == "insult":
      reply = "Sure, who do you want me to insult?"

    else:
      victim = " ".join((command.split(" "))[1:])
      reply += random.choice(responses.INSULT(victim))
  
  # joke
  elif command.startswith("joke"):

    if command == "joke":
      reply += random.choice(responses.JOKE())

    elif command.startswith("joke about"):
      victim = " ".join((command.split(" "))[2:])
      reply += random.choice(responses.INSULT(victim))

    else:
      reply += random.choice(responses.JOKE())
  
  # love
  elif command == "love" or command == "i love you":
    reply += random.choice(responses.LOVE())

  # magic
  elif command == "magic" or command == "magic trick" or command == "abracadabra":
    reply += random.choice(responses.MAGIC())
  
  # scream
  elif command == "scream":
    reply += random.choice(responses.SCREAM())

  # serve
  elif command.startswith("serve"):

    if command == "serve":
      reply += "Sure, which drink do you want me to serve?"

    elif command == "serve beer":
      reply += random.choice(responses.SERVE("beer"))
      reply += " :beer:"

    elif command == "serve boba" or command == "serve bubble tea":
      reply += random.choice(responses.SERVE("bubble tea"))
      reply += " :bubble_tea:"

    elif command == "serve cocktail":
      reply += random.choice(responses.SERVE("cocktail"))
      reply += " :cocktail:"
    
    elif command == "serve coffee":
      reply += random.choice(responses.SERVE("coffee"))
      reply += " :coffee:"

    elif command == "serve juice":
      fruits = ["orange", "apple", "pineapple", "guava", "raspberry", "cranberry", "mango", "litchi", "pear", "lemon", "mixed fruit", "blueberry"]
      reply += random.choice(responses.SERVE(random.choice(fruits) + " juice"))
      reply += " :tropical_drink:"

    elif command == "serve milk":
      reply += random.choice(responses.SERVE("milk"))
      reply += " :milk:"
    
    elif command == "serve soda":
      reply += random.choice(responses.SERVE("soda"))
      reply += " :tumbler_glass:"

    elif command == "serve tea":
      reply += random.choice(responses.SERVE("tea"))
      reply += " :tea:"
    
    elif command == "serve water":
      reply += random.choice(responses.SERVE("water"))
      reply += " :cup_with_straw:"

    elif command == "serve wine":
      reply += random.choice(responses.SERVE("wine"))
      reply += " :wine_glass:"
  
    else:
      return exceptions.PROMPT["missing_recipe"]

  # sing
  elif command == "sing" or command == "sing song" or command == "sing a song":
    reply += random.choice(responses.SING())

  # confusion
  else:
    reply += random.choice(responses.CONFUSE())

  return reply
