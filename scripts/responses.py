# Local application imports
from scripts import exceptions

# ----- Card Based Commands -----

def CHANGELOG():
  date_path = './pages/changelog/date.txt'
  add_path = './pages/changelog/add.txt'
  fix_path = './pages/changelog/fix.txt'

  card = {
    'date' : "???",
    'add' : "???",
    'fix' : "???",
  }

  try:
    with open(date_path, 'r') as file:
      card['date'] = file.read()
  
    with open(add_path, 'r') as file:
      card['add'] = file.read()
  
    with open(fix_path, 'r') as file:
      card['fix'] = file.read()

  except FileNotFoundError as e:
    print("--- Missing changelog ---")

  return card
    

def HELP():
  desc_path = './pages/manual/desc.txt'
  note_path = './pages/manual/note.txt'
  list_path = './pages/manual/list.txt'
  foot_path = './pages/manual/foot.txt'

  card = {
    'desc' : "???",
    'note' : "???",
    'list' : "???",
    'foot' : "???",
  }

  try:
    with open(desc_path, 'r') as file:
      card['desc'] = file.read()
  
    with open(note_path, 'r') as file:
      card['note'] = file.read()
  
    with open(list_path, 'r') as file:
      card['list'] = file.read()
  
    with open(foot_path, 'r') as file:
      card['foot'] = file.read()

  except FileNotFoundError as e:
    print("--- Missing manual ---")

  return card
    

def MENU():
  desc_path = './pages/menu/desc.txt'
  food_path = './pages/menu/food.txt'
  drink_path = './pages/menu/drink.txt'

  card = {
    'desc' : "???",
    'food' : "???",
    'drink' : "???",
  }

  try:
    with open(desc_path, 'r') as file:
      card['desc'] = file.read()

    with open(food_path, 'r') as file:
      card['food'] = file.read()

    with open(drink_path, 'r') as file:
      card['drink'] = file.read()

  except FileNotFoundError as e:
    print("--- Missing menu ---")

  return card

def ROLL():
  desc_path = './pages/roll/desc.txt'

  card = {
    'desc' : "???",
  }

  try:
    with open(desc_path, 'r') as file:
      card['desc'] = file.read()

  except FileNotFoundError as e:
    print("--- Missing rolls ---")

  return card

def BALL():
  desc_path = './pages/ball/desc.txt'
  list_path = './pages/ball/list.txt'

  card = {
    'desc' : "???",
    'list' : []
  }

  try:
    with open(desc_path, 'r') as file:
      card['desc'] = file.read()

    with open(list_path, 'r') as file:
      card['list'] = [item for item in file.read().split("\n") if item]

  except FileNotFoundError as e:
    print("--- Missing 8ball ---")

  return card


# ----- Chat Based Commands -----


def WAIT():
  try:
    msg_path = './messages/wait.txt' 
    with open(msg_path, 'r') as file:
      return file.read().split("\n")

  except FileNotFoundError as e:
    return [ exceptions.PROMPT["unable"] ]


def GOODBYE():
  try:
    msg_path = './messages/goodbye.txt'
    with open(msg_path, 'r') as file:
      return file.read().split("\n")

  except FileNotFoundError as e:
    return [ exceptions.PROMPT["unable"] ]

def GREET():
  try:
    msg_path = './messages/greet.txt'
    with open(msg_path, 'r') as file:
      return file.read().split("\n")

  except FileNotFoundError as e:
    return [ exceptions.PROMPT["unable"] ]


def ORDER(food):
  try:
    msg_path = './messages/order.txt'
    with open(msg_path, 'r') as file:
      return file.read().format(food = food).split("\n")

  except FileNotFoundError as e:
    return [ exceptions.PROMPT["unable"] ]


def JOKE():
  try:
    msg_path = './messages/joke.txt'
    with open(msg_path, "r") as file:
      return file.read().split("\n")

  except FileNotFoundError as e:
    return [ exceptions.PROMPT["unable"] ]


def INSULT(victim):
  try:
    msg_path = './messages/insult.txt'
    with open(msg_path, 'r') as file:
      return file.read().format(victim = victim).split("\n")
  
  except FileNotFoundError as e:
    return [ exceptions.PROMPT["unable"] ]


def LOVE():
  try:
    msg_path = './messages/love.txt'
    with open(msg_path, 'r') as file:
      return file.read().split("\n")

  except FileNotFoundError as e:
    return [ exceptions.PROMPT["unable"] ]


def CONFUSE():
  try:
    msg_path = './messages/confuse.txt'
    with open(msg_path, 'r') as file:
      return file.read().split("\n")

  except FileNotFoundError as e:
    return [ exceptions.PROMPT["unable"] ]


def EXPLODE(victim):
  try:
    msg_path = './messages/explode.txt'
    with open(msg_path, "r") as file:
      return file.read().format(victim = victim).split("\n")

  except FileNotFoundError as e:
    return [ exceptions.PROMPT["unable"] ]
    

def SERVE(drink):
  try:
    msg_path = './messages/serve.txt'
    with open(msg_path, 'r') as file:
      return file.read().format(drink = drink).split("\n")

  except FileNotFoundError as e:
    return [ exceptions.PROMPT["unable"] ]
  

def HRU():
  try:
    msg_path = './messages/hru.txt'
    with open(msg_path, "r") as file:
      return file.read().split("\n")
  
  except FileExistsError as e:
    return [ exceptions.PROMPT["unable"] ]
  

# ----- Removed Commands -----
  
def SING():
  try:
    msg_path = './messages/sing.txt'
    with open(msg_path, "r") as file:
      return file.read().split("\n")

  except FileNotFoundError as e:
    return [ exceptions.PROMPT["unable"] ]
  

def MAGIC():
  try:
    msg_path = './messages/magic.txt'
    with open(msg_path, "r") as file:
      return file.read().split("\n")

  except FileNotFoundError as e:
    return [ exceptions.PROMPT["unable"] ]
  

def DANCE():
  try:
    msg_path = './messages/dance.txt'
    with open(msg_path, 'r') as file:
      return file.read().split("\n")

  except FileNotFoundError as e:
    return [ exceptions.PROMPT["unable"] ]
  

def SCREAM():
  try:
    msg_path = './messages/scream.txt'
    with open(msg_path, 'r') as file:
      return file.read().split("\n")

  except FileNotFoundError as e:
    return [ exceptions.PROMPT["unable"] ]