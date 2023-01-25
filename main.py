import discord
import discord.py


# - - - - Initialize - - - - #
intents = discord.Intents().all()
thor = discord.Client()


# - - - - - Start - - - - - #
print('''placeholder''')
ScriptQues = input('Do You Want To Continue (yes/no): ')

if ScriptQues.lower == 'yes':
  pass
else:
  end


print('''placeholder''')
token = input("Token: ")

# - - - - Commands - - - - #
@thor.event
async def on_ready():
  os.system('clear')
  os.system('cls')
  print('''placeholder''')
  print(f'Made By: Qouda and Mali')
  print(f'Logged in as {client.user}')



client.run(token, bot=False)
