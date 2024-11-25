# Standard library imports
import random
import discord
import datetime
import re

# Local application imports
from scripts import exceptions
from scripts import responses

# Global variables
devmode = "???"
client = "???"
launch_time = "???"

# Init bot variables
def begin(session):
  global devmode
  global client
  global launch_time

  devmode = session['devmode']
  launch_time = session['launch_time']
  client = session['client']
  print("Launched on--> " + str(launch_time)) 

# Parse all statements
def parse(message):
  content = message.content.lower()
  content = content.strip()

  punc = '''!()[]{};:'"\\,<>./?@#$%^&*_~'''

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

  elif command == "status":
      embed = discord.Embed(
          color=discord.Color.green()
      )

      server_count = len(client.guilds)
      latency = round(client.latency * 1000)

      embed.add_field(name="🔧 Devmode", value="Enabled" if devmode else "Disabled", inline=False)
      embed.add_field(name="🚀 Launch", value=launch_time.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
      embed.add_field(name="⏳ Uptime", value=str(datetime.datetime.now() - launch_time).split('.')[0], inline=False)
      embed.add_field(name="📡 Latency", value=f"{latency} ms", inline=False)
      embed.add_field(name="🌐 Servers", value=f"{server_count} live servers", inline=False)

  # roll
  elif command.startswith("roll"):
    card = responses.ROLL()
    ledger = ""
    score = 0

    if command == "roll":
      embed = discord.Embed(
        color = discord.Color.purple()
      )
      embed.add_field(name = 'Specifying roll attributes', value = card['desc'], inline = True)
    
    else:
      option = command.split(" ")[1]
      match = re.match(r"([0-9]+)d([0-9]+)(((\+|-)[0-9]+)?)", option)
      embed = discord.Embed()

      if match:
          modif = 0
          count = int(match.group(1))
          sides = int(match.group(2))

          for i in range(count): 
            value = random.randint(1,sides)
            ledger = ledger + " + " + str(value)
            score = score + value

          if (match.group(3)):
            sign = match.group(3)[0]
            modif = int(match.group(3)[1::])

            if (sign == '+'):
              score = score + modif
              ledger = ledger + " + " + str(modif)
            elif (sign == '-'):
              score = score - modif
              ledger = ledger + " - " + str(modif)

          if (count > 1 or modif != 0):
            ledger = ledger + " = "
            ledger = ledger[2::]
          else:
            ledger = ""

          embed = discord.Embed(
            description = "roll: " + ledger + str(score),
            color = discord.Color.purple()
          )
      
      else:
          embed = discord.Embed(
          color = discord.Color.purple()
          )
          embed.add_field(name = 'Specifying roll attributes', value = card['desc'], inline = True)

  # 8ball
  elif command.startswith("8ball"):
    card = responses.BALL()

    if command == "8ball":
      embed = discord.Embed(
        color = discord.Color.purple()
      )
      embed.add_field(name = 'Asking questions with 8ball', value = card['desc'], inline = True)
    
    else:

      num = random.randint(1,20)
      if num <= 10:
        clr = discord.Color.green()
      elif num <= 15:
        clr = discord.Color.yellow()
      else:
        clr = discord.Color.red()

      embed = discord.Embed(
        description = "8ball: " + card['list'][num],
        color = clr
      )

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

  # hru
  elif command == "hru" or command == "how are you":
    reply = random.choice(responses.HRU())

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

  # confusion
  else:
    reply += random.choice(responses.CONFUSE())

  return reply
