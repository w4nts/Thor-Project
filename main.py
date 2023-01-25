import discord
import discord.py


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

if ScriptQues.lower == 'yes':
  pass
else:
  end


os.system('clear')
os.system('cls')
print(thorascii)
prefix = input('prefix: ')
intents = discord.Intents().all()
thor = commands.Bot(command_prefix=prefix, self_bot=True)
client.remove_command('help')

# - - - - - Start - - - - - #
os.system('clear')
os.system('cls')
print(thorascii)
token = input("Token: ")

# - - - - Commands - - - - #
@thor.event
async def on_ready():
  os.system('clear')
  os.system('cls')
  print(thorascii)
  print(f'Made By: Qouda and Mali')
  print(f'Logged in as {client.user}')


client.run(token, bot=False)
