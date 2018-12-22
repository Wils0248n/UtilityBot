import random, asyncio, discord, re
from discord.ext import commands
from discord.ext.commands import Bot

class UtilityBot():

	def __init__(self):
		self.bot = commands.Bot(command_prefix='!')

	async def clear_channel(self, channel):
		async for msg in self.bot.logs_from(channel):
			try:
				await self.bot.delete_message(msg)
			except discord.errors.Forbidden:
				await self.bot.send_message(channel, 'Missing Permissions')
				break

	async def clear_channel_with_word(self, channel, word):
		async for msg in self.bot.logs_from(channel):
			try:
				if word in msg.content:
					await self.bot.delete_message(msg)
			except discord.errors.Forbidden:
				await self.bot.send_message(channel, 'Missing Permissions')
				break

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

	async def get_embed_message(self):
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
		dev = await self.bot.get_user_info(259624839604731906)
		embed_message.set_footer(text = 'Developer: ' + dev.name + "#" + dev.discriminator)
		return embed_message
