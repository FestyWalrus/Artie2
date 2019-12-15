from discord.ext import commands
import datetime

requiredTrigger = 'artie'
timeTrigger = 'time'

class TimeDate(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message): #when a message is read by the bot...
		if message.author == self.bot.user: #stop if the message came from the bot
			return

		if message.content.find(requiredTrigger) != -1: #if the trigger (bot's name) is found, process command triggers
			
			if message.content.find(timeTrigger) != -1: #if the time trigger activates...
				now = datetime.datetime.now()
				timeString = "The current time is " + str(now.hour) + ":" + str(now.minute) + " EST."
				await message.channel.send(timeString) #send the current time

def setup(bot):
	bot.add_cog(TimeDate(bot))

