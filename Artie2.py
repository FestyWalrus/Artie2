import discord
from discord.ext import commands

extensions = ["commandsets.timedate"]

bot = commands.Bot(command_prefix='a.', description="idk lul")


@bot.event
async def on_ready():
	print("logged in")
	bot.load_extension(extensions[0])

bot.run('NTMxMTMyNDUwMzQxMTI2MTY0.XdiE9A._wVboHkdVYiGMFL4nxcZPkp7w9s')

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




