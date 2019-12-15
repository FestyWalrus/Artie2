import discord
from discord.ext import commands
from os import walk

bot = commands.Bot(command_prefix='a.', description="A bot you can talk to..just say \"Artie\" so they know you're talking to them :)") #define the bot

tokenFile = open("token.txt", "r+") #read or create the bot token file

def load_extensions(firstLoad): #loads extensions in the commandsets directory
	extensions = []

	if firstLoad:
		print("Loading extensions...")
	else:
		print("Reloading extensions...")

	for (dirpath, dirnames, filenames) in walk("commandsets"):
		extensions.extend(filenames) #add every file in commandsets directory to extensions list
		break

	for cmdNameIndex in range(len(extensions)):
		extensionPosition = extensions[cmdNameIndex].find(".py")
		if extensionPosition == -1:
			del extensions[cmdNameIndex] #delete any file from extensions list that isn't an extension
		else:
			extensions[cmdNameIndex] = extensions[cmdNameIndex].split(".py", 1)[0]
			try:
				bot.load_extension("commandsets." + extensions[cmdNameIndex]) #try to load extension
				print("   Loaded " + extensions[cmdNameIndex])
			except Exception as e:
				print("   Failed to load extension " + extensions[cmdNameIndex] + ": ", end="") #print error if an extension won't load
				print(e)

@bot.event
async def on_ready(): #when bot is connected...
	print("Logged into Discord")
	tokenFile.close()
	load_extensions(True)
	print("All set :3")

print("Artie 2: the Discord bot you can talk to.")

try:
	bot.run(tokenFile.read().strip()) #read the token from the token.txt file and try to connect
except Exception as e:
	print("Failed to connect to Discord: ", end="") #print error if bot cannot connect
	print(e)
