import discord
from discord.ext import commands
from os import walk

#extensions = ["commandsets.timedate"]

extensions = []



bot = commands.Bot(command_prefix='a.', description="idk lul")

def load_extensions(firstLoad):

	if firstLoad:
		print("Loading extensions...")
	else:
		print("Reloading extensions...")

	for (dirpath, dirnames, filenames) in walk("commandsets"):
		extensions.extend(filenames)
		break

	for commandName in range(len(extensions)):
		extensionPosition = extensions[commandName].find(".py")
		if extensionPosition == -1:
			del extensions[commandName]
		else:
			extensions[commandName] = extensions[commandName].split(".py", 1)[0]
			
			try:
				bot.load_extension("commandsets." + extensions[commandName])
				print("Loaded " + extensions[commandName])
			except Exception as e:
				print("Failed to load extension " + extensions[commandName] + ": ", end="")
				print(e)

@commands.command(#broken
	name='reload',
	description='reloads extensions',
	aliases=[]
	)

async def reload_command(ctx):#broken
	load_extensions(False)

@bot.event
async def on_ready():
	print("logged in")
	load_extensions(True)
	'''while(True):
		debugCommand = input("ArtieDebugConsole>")
		if debugCommand == "reload":
			load_extensions(False)'''
	

bot.run('NTMxMTMyNDUwMzQxMTI2MTY0.Xef9uQ.sJbdMebJgmFlO7e8ROsFP6rNfRU')




'''class ArtieClient(discord.Client):
	async def on_message(self, message):
		#ignore messages from the bot
		if message.author == self.user:
			return

		#await message.channel.send(message.content)

artie = ArtieClient()
	
if __name__ == '__main__':
	for extension in extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			print("Failed to load extension.")
			print(e)
'''




