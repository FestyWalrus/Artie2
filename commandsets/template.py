'''
	Template commandset for Artie
	By default this commandset will do nothing; it's just meant
	as a starting point for making Artie commandsets.

	Made by Riley Knybel
	Steal this code I literally don't care
'''

from discord.ext import commands

requiredTrigger = 'artie'

class Template(commands.Cog): #change this to match the command name

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message): #when a message is read by the bot...

		if message.author == self.bot.user: #stop if the message came from the bot
			return

		if message.content.find(requiredTrigger) != -1: #if the trigger (bot's name) is found, process command triggers
			#command checks and code go here
			return

def setup(bot):
	bot.add_cog(Template(bot)) #remember to change this to the name of the command class above
