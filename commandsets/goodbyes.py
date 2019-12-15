'''
	Goodbyes
	Sends a random response to several types of farewells

	Made by Riley Knybel
	Steal this code I literally don't care
'''

import random
from discord.ext import commands

requiredTrigger = 'artie'
goodbyes = ['bye', 'goodbye', 'cya', 'laters', 'bye-bye', 'so long', 'I\'ll miss you', 'good night', 'later']

class Goodbyes(commands.Cog): #change this to match the command name

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message): #when a message is read by the bot...

		if message.author == self.bot.user: #stop if the message came from the bot
			return

		if message.content.lower().find(requiredTrigger) != -1: #if the trigger (bot's name) is found, process command triggers
			#command checks and code go here
			for goodbye in goodbyes:
				if message.content.lower().find(goodbye) != -1:
					await message.channel.send(random.choice(goodbyes).capitalize() + "!")
					return

def setup(bot):
	bot.add_cog(Goodbyes(bot)) #remember to change this to the name of the command class above
