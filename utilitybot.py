import random, asyncio, discord, re, time, sys
from discord.ext import commands
from discord.ext.commands import Bot

class UtilityBot():

	def __init__(self):
		self.bot = commands.Bot(command_prefix='!')

	def flip(self):
		return random.choice(["Heads", "Tails"])

	def roll(self):
		return str(random.randint(1, 6))

	def OwOify(self, text):
		faces = ["OwO", "UwU", ">w<", "^w^"]
		text = re.sub('!owo', '', text)
		text = re.sub(r'(?:r|l)', 'w', text)
		text = re.sub(r'(?:R|L)', 'W', text)
		text = re.sub(r'n([aeiou])', r'ny\1', text)
		text = re.sub(r'N([aeiou])', r'Ny\1', text)
		text = re.sub(r'N([AEIOU])', r'Ny\1', text)
		text = re.sub(r'ove', 'uv', text)
		text = re.sub(r'\!+', " " + random.choice(faces) + " ", text)
		return text

	def get_embed_message(self, dev):
		embed_message = discord.Embed()
		embed_message.title = 'Wilsøn\'s UtilityBot'
		embed_message.color = 16496176
		embed_message.description = 'UtilityBot provides general utility functions to the discord server'
		embed_message.add_field(name='Commands', value="\
		!flip -> Flips a coin.\n \
		!roll -> rolls a six sided dice.\n \
		!owo -> Defiles the proceeding message.\n \
		!clear -> clears a text channel.\n \
		!clear <word> -> clears messages that contain <word>.", inline=False)
		embed_message.add_field(name='Source', value='https://github.com/Wils0248n/UtilityBot', inline=False)
		embed_message.set_image(url='https://i.imgur.com/FQTjdml.png')
		embed_message.set_thumbnail(url='https://i.imgur.com/dgLpgLc.png')
		embed_message.set_footer(text = 'Developer: ' + dev.name + "#" + dev.discriminator)
		return embed_message

utilitybot = UtilityBot()

def main():
		while True:
			try:
				utilitybot.bot.loop.run_until_complete(utilitybot.bot.start(sys.argv[1]))
			except IndexError:
				print("You must enter a bot token.\n")
				print("Usage: python3 utilitybot.py <bot-token>")
				sys.exit(1)
			except discord.errors.LoginFailure:
				print("Invalid bot token.\n")
				sys.exit(1)
			except KeyboardInterrupt:
				print("\nExitting Gracefully")
				utilitybot.bot.close()
				sys.exit(0)

@utilitybot.bot.event
async def on_message(message):
	if message.content == '!utilitybot':
		dev = utilitybot.bot.get_user(259624839604731906)
		await message.channel.send(embed=utilitybot.get_embed_message(dev))

	if message.content == '!flip':
		await message.channel.send("Coin Flipped: " + utilitybot.flip())

	if message.content == '!roll':
		await message.channel.send("Dice Rolled: " + utilitybot.roll())

	if message.content == '!clear':
		try:
			await message.channel.purge()
		except discord.errors.Forbidden:
			await message.channel.send('Missing Permissions')

	if message.content.startswith('!clear '):
		try:
			content = message.content.split(' ')[1]
			await message.channel.purge(check=content)
		except discord.errors.Forbidden:
			await message.channel.send('Missing Permissions')

	if message.content.startswith('!owo '):
		await message.channel.send("OwO notcies your message: " + utilitybot.OwOify(message.content))



@utilitybot.bot.event
async def on_ready():
	print(utilitybot.bot.user.name+ ' Ready!')
	await utilitybot.bot.change_presence(activity=discord.Activity(game=discord.Game(name="Utilitybot | !utilitybot")))

if __name__ == '__main__':
	main()
