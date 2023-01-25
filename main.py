import discord
import discord.py

intents = discord.Intents().all()
thor = discord.Client()

print('''placeholder''')
ScriptQues = input('Do You Want To Continue (yes/no): ')

if ScriptQues.lower == 'yes':
  pass
else:
  end

print('''placeholder''')
token = input("Token: ")
@thor.event
async def on_ready():
  os.system('clear')
  os.system('cls')
  print('''placeholder''')
  print(f'Made By: Qouda and Mali')
  print(f'Logged in as {client.user}')



client.run(token, bot=False)
