import discord
import os
from discord.ext import commands
from discord.ext.commands import *
os.system('pip install discord==1.0.1')
os.system('pip install discord.py==1.6.0')

thorascii = ('''    ████████╗██╗  ██╗ ██████╗ ██████╗ 
    ╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗
       ██║   ███████║██║   ██║██████╔╝
       ██║   ██╔══██║██║   ██║██╔══██╗
       ██║   ██║  ██║╚██████╔╝██║  ██║
       ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
                                      ''')

# - - - - Initialize - - - - #
os.system('clear')
os.system('cls')
print(thorascii)
ScriptQues = input('Do You Want To Continue (yes/no): ')

if ScriptQues.lower() == 'yes':
  pass
else:
  quit()


os.system('clear')
os.system('cls')
print(thorascii)
prefix = input('prefix: ')
intents = discord.Intents().all()
thor = commands.Bot(command_prefix=prefix, self_bot=True)
thor.remove_command('help')

# - - - - - Start - - - - - #
os.system('clear')
os.system('cls')
print(thorascii)
token = input('Token: ')

# - - - - Commands - - - - #
@thor.event
async def on_ready():
  os.system('clear')
  os.system('cls')
  print(thorascii)
  print('Made By: Qouda and Mali\nhttps://github.com/w4nts/thor-project')
  print(f'Logged in as {thor.user}')


thor.run(token, bot=False)
